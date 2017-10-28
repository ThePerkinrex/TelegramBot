import Utils


def handleMessage(update):
    print('UPDATE: ' + str(update))

    r = 'Error'

    message = update['message']
    if message['text'] == '/stop':
        r = [('stopping bot', {})]
        exit(0)
    else:
        if message['chat']['type'] == 'group':
            keyboard = Utils.get_test_keyboard()
            # print(keyboard)
            r = [('Tell me A or B', keyboard)]
        else:
            r = [('You told me "' + message['text'] + '"', {})]
            print('MSG_RESPONSE: ' + str(update['update_id']))

    return r
