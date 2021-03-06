import Utils
import re

import bot_token

polls = []
pollsInEdit = []

def handle_message(update, lang):
    # print('UPDATE: ' + str(update))
    Utils.log_mess('UPDATE', str(update), Utils.LogColors.OKBLUE)

    r = [(Utils.inte('cancreatepolls', lang), {})]

    message = update['message']
    if message['text'] == '/stop' or message['text'] == '/stop@' + bot_token.bot_id:
        r = ['NONE', 'NONE']
    else:
        if message['chat']['type'] == 'group':

            # keyboard = Utils.generate_poll(len(polls), ['A', 'B'])
            # polls.append({'title': 'Tell me A or B', 'A': 0, 'B': 0})
            # print(keyboard)
            # r = [('Tell me A or B', keyboard)]
            # print('MSG_RESPONSE: ' + str(update['update_id']))
            regex1 = re.match(Utils.inte('question', lang).lower() + ' (.+)', message['text'].lower())
            regex2 = re.split('\s*,\s*', message['text'])
            regex3 = re.match(Utils.inte('end_poll', lang) + ' (\d+)', message['text'].lower())  # FIXME: This regex
            # print('MSG_HANDLER: MSG IS ' + message['text'])
            Utils.log_mess('MSG_HANDLER', 'MSG is ' + message['text'])
            if message['text'].lower() == Utils.inte('createpoll', lang).lower():
                # print('POLLS: CREATE POLL1')
                Utils.log_mess('POLLS', 'Create poll #1', Utils.LogColors.OKGREEN)
                pollsInEdit.append({'username': message['from']['username'], 'chat': message['chat']['id']})
                r = [(Utils.inte('what_question', lang) + '\n' + Utils.inte('answer_what_q', lang), {})]

            elif regex1:
                # print('POLLS: CREATE POLL2')
                Utils.log_mess('POLLS', 'Create poll #2', Utils.LogColors.OKGREEN)
                for poll in pollsInEdit:
                    if poll['username'] == message['from']['username'] and poll['chat'] == message['chat']['id']:
                        pollsInEdit[pollsInEdit.index(poll)].update({'title': regex1.group(1)})

                        r = [(Utils.inte('answer_comma', lang), {})]
                        break
            elif len(regex2) > 0:
                # print('POLLS: CREATE POLL3')
                Utils.log_mess('POLLS', 'Create poll #3', Utils.LogColors.OKGREEN)
                for poll in pollsInEdit:
                    if poll['username'] == message['from']['username'] and poll['chat'] == message['chat']['id']:
                        respo = {}
                        for option in regex2:
                            respo.update({option: 0})

                        pollsInEdit[pollsInEdit.index(poll)].update({'options': respo})
                        polls.append(pollsInEdit[pollsInEdit.index(poll)])
                        pollsInEdit.remove(pollsInEdit[pollsInEdit.index(poll)])
                        r = [(Utils.inte('poll_ok', lang), {}),
                             (Utils.inte('poll', lang) + ' #' + str(polls.index(poll)) + ': ' + poll['title'],
                              Utils.generate_poll(polls.index(poll),
                                                  list(poll['options'].keys())))]
                        break
            elif regex3:
                Utils.log_mess('POLLS', 'END POLL', Utils.LogColors.OKGREEN)
                n = int(regex3.group(1))
                if n < len(polls):
                    # end_poll = polls.pop(n)
                    pass

            else:
                r = [(Utils.inte('cancreatepolls', lang), {})]
        else:
            r = [(Utils.inte('told_me', lang) + ' "' + message['text'] + '"', {})]

    # print('MSG_RESPONSE: ' + str(update['update_id']))
    Utils.log_mess('MSG_RESPONSE', str(update['update_id']))
    # print('MSG_RESPONSE: ' + str(r))
    Utils.log_mess('MSG_RESPONSE', str(r))
    # print('POLLS: In edit ' + str(pollsInEdit))
    Utils.log_mess('POLLS', 'In edit ' + str(pollsInEdit), Utils.LogColors.OKGREEN)
    return r


def handle_callback(update):
    callback = update['callback_query']
    # print('CALLBACK_RESPONSE: ' + str(update['update_id']))
    Utils.log_mess('CALLBACK', 'Response to ' + str(update['update_id']), Utils.LogColors.OKBLUE)
    poll_id = int(callback['data'].split(':::')[0])
    option = callback['data'].split(':::')[1]

    polls[poll_id]['options'][option] += 1

    # print('POLLS: ' + str(polls))
    Utils.log_mess('POLLS', str(polls), Utils.LogColors.OKGREEN)
    return Utils.send_callback(callback['id'], {}).json()
