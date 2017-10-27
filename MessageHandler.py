import Utils


def handleMessage(update):
    print(update)

    r = 'Error'

    message = update['message']
    if message['text'] == '/stop':
        r = ['stopping bot']
        exit(0)
    else:
        if message['chat']['type'] == 'group':
            keyboard = Utils.get_test_keyboard()
            print(keyboard)
            r = [('Hello ' + message['from']['first_name'], {}),
                 ('Tell me A or B', keyboard)]
        else:
            r = [('You told me "' + message['text'] + '"', {})]
            print('Answering ' + str(update['update_id']))

    for message in r:
        if len(message) is 1:
            Utils.send_mess(Utils.get_chat_id(update), message[0])
        elif len(message) is 2:
            Utils.send_mess(Utils.get_chat_id(update), message[0], message[1])
        else:
            Utils.send_mess(Utils.get_chat_id(update), 'Error len(message) --> ' + str(len(message)) + '; message --> ' + message)

    return r
