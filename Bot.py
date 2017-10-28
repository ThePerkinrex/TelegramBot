import MessageHandler as MHandler
import Utils


url = "https://api.telegram.org/bot479189806:AAFgwI7drgzRoXTGnoCxgrFyfWcUxKP1Wlc/"


# chat_id = Utils.get_chat_id(Utils.last_update(Utils.get_updates_json(url)))
# Utils.send_mess(chat_id, 'Telegram Bot On')


def stop_bot():
    print('END_PRC: STOPPING BOT')
    exit(0)


def main():
    if Utils.last_update(Utils.get_updates_json(url)) is None:
        update_id = 1
    else:
        update_id = Utils.last_update(Utils.get_updates_json(url))['update_id']
    while True:
        try:
            update = Utils.last_update(Utils.get_updates_json(url, update_id))
            if update is not None:
                if update.get('message'):
                    # Utils.send_mess(Utils.get_chat_id(update), MHandler.handleMessage(update))
                    r = MHandler.handle_message(update)
                    print('HANDLED_MSG: ' + str(r))
                    response = 'none'
                    for mess in r:
                        print('MSG: ' + str(mess))
                        if mess == 'NONE':
                            response = None
                            break
                        else:
                            response = Utils.send_mess(Utils.get_chat_id(update), mess[0], mess[1])
                    if response:
                        print('RESPONSE: ' + str(response.json()))
                    else:
                        print('STOPPING')
                        stop_bot()
                elif update.get('callback_query'):
                    callback_query = update.get('callback_query')
                    print('CALLBACK_QUERY: ' + str(callback_query))
                    r = MHandler.handle_callback(update)
                    print('CALLBACK: ' + str(r))

                    # name = 'You'
                    # if callback_query.get('from').get('username'):
                    #     name = '@' + callback_query['from']['username']
                    # elif callback_query.get('from').get('first_name'):
                    #     name = callback_query.get('from').get('first_name')
                    # Utils.send_mess(callback_query['message']['chat']['id'], name + ' told me ' + callback_query['data'])
                update_id = Utils.last_update(Utils.get_updates_json(url))['update_id'] + 1
        except KeyboardInterrupt:
            stop_bot()


if __name__ == '__main__':
    main()
