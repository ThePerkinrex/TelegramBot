import Utils

polls = []


def handle_message(update):
    print('UPDATE: ' + str(update))

    r = 'Error'

    message = update['message']
    if message['text'] == '/stop':
        r = ['NONE', 'NONE']
    else:
        if message['chat']['type'] == 'group':
            keyboard = Utils.generate_poll(len(polls), ['A', 'B'])
            polls.append(['A', 'B'])
            # print(keyboard)
            r = [('Tell me A or B', keyboard)]
            print('MSG_RESPONSE: ' + str(update['update_id']))
        else:
            r = [('You told me "' + message['text'] + '"', {})]
            print('MSG_RESPONSE: ' + str(update['update_id']))

    return r


def handle_callback(update):
    callback = update['callback_query']
    print('CALLBACK_RESPONSE: ' + str(update['update_id']))
    return Utils.send_callback(callback['id'], {})
