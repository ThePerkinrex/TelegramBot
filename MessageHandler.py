import Bot


def handleMessage(update):
    print(update)

    message = update['message']
    if message['text'] == '/stop':
        Bot.send_mess(Bot.get_chat_id(update), 'Stopping Chatbot')
        exit(0)
    else:
        if message['chat']['type'] == 'group':
            messageToSend = 'Hello ' + message['from']['first_name']
            Bot.send_mess(Bot.get_chat_id(update), messageToSend)
            Bot.send_mess(Bot.get_chat_id(update), 'You told me "' + message['text'] + '"')
        else:
            Bot.send_mess(Bot.get_chat_id(update), 'You told me "' + message['text'] + '"')
            print('Answering ' + str(update['update_id']))
