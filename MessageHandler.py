import Utils
import re

polls = []
pollsInEdit = []


def handle_message(update):
    print('UPDATE: ' + str(update))

    r = [('I can crete polls', {})]

    message = update['message']
    if message['text'] == '/stop':
        r = ['NONE', 'NONE']
    else:
        if message['chat']['type'] == 'group':

            # keyboard = Utils.generate_poll(len(polls), ['A', 'B'])
            # polls.append({'title': 'Tell me A or B', 'A': 0, 'B': 0})
            # print(keyboard)
            # r = [('Tell me A or B', keyboard)]
            # print('MSG_RESPONSE: ' + str(update['update_id']))
            regex1 = re.match('la pregunta es (.+)', message['text'].lower())
            regex2 = re.split('\s*,\s*', message['text'])
            print('MSG_HANDLER: MSG IS ' + message['text'])
            if message['text'].lower() == 'crea una encuesta':
                print('POLLS: CREATE POLL1')
                pollsInEdit.append({'username': message['from']['username'], 'chat': message['chat']['id']})
                r = [('¿Cuál es la pregunta?\nResponde como "La pregunta es ..."', {})]

            elif regex1:
                print('POLLS: CREATE POLL2')
                for poll in pollsInEdit:
                    if poll['username'] == message['from']['username'] and poll['chat'] == message['chat']['id']:
                        pollsInEdit[pollsInEdit.index(poll)].update({'title': regex1.group(1)})

                        r = [('Ahora dime las opciones separadas por comas', {})]
                        break
            elif len(regex2) > 0:
                print('POLLS: CREATE POLL3')
                for poll in pollsInEdit:
                    if poll['username'] == message['from']['username'] and poll['chat'] == message['chat']['id']:
                        respo = {}
                        for option in regex2:
                            respo.update({option: 0})

                        pollsInEdit[pollsInEdit.index(poll)].update({'options': respo})
                        polls.append(pollsInEdit[pollsInEdit.index(poll)])
                        pollsInEdit.remove(pollsInEdit[pollsInEdit.index(poll)])
                        r = [('Bien, se ha creado la encuesta', {}), ('Encuesta: ' + poll['title'],
                                                                 Utils.generate_poll(polls.index(poll),
                                                                                     list(poll['options'].keys())))]
                        break
            else:
                r = [('I can crete polls', {})]
        else:
            r = [('You told me "' + message['text'] + '"', {})]

    print('MSG_RESPONSE: ' + str(update['update_id']))
    print('MSG_RESPONSE: ' + str(r))
    print('POLLS: In edit ' + str(pollsInEdit))
    return r


def handle_callback(update):
    callback = update['callback_query']
    print('CALLBACK_RESPONSE: ' + str(update['update_id']))

    poll_id = int(callback['data'].split(':::')[0])
    option = callback['data'].split(':::')[1]

    polls[poll_id]['options'][option] += 1

    print('POLLS: ' + str(polls))
    return Utils.send_callback(callback['id'], {}).json()
