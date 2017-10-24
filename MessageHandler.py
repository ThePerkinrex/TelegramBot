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
            r = ['Hello ' + message['from']['first_name'], 'You told me "' + message['text'] + '"']
        else:
            r = ['You told me "' + message['text'] + '"']
            print('Answering ' + str(update['update_id']))

    return r
