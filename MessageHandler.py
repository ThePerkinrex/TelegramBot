import Utils


def handleMessage(update):
    print(update)

    r = 'Error'

    message = update['message']
    if message['text'] == '/stop':
        Utils.send_mess(Utils.get_chat_id(update), 'Stopping Chatbot')
        exit(0)
    else:
        if message['chat']['type'] == 'group':
            r = ['Hello ' + message['from']['first_name'], 'You told me "' + message['text'] + '"']
        else:
            r = [Utils.get_chat_id(update), 'You told me "' + message['text'] + '"']
            print('Answering ' + str(update['update_id']))

    return r
