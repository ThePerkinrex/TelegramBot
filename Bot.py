import sys
import traceback

import MessageHandler as MHandler
import Utils


url = Utils.url
lang = 'en-US'
validlang = ['en-US', 'es-ES']

args = sys.argv
# print('PASSED ARGS: ' + str(args))

if args[1] in validlang:
    lang = args[1]



# chat_id = Utils.get_chat_id(Utils.last_update(Utils.get_updates_json(url)))
# Utils.send_mess(chat_id, 'Telegram Bot On')


def stop_bot():
    # print('END_PRC: STOPPING BOT')
    Utils.log_mess('END_PRC', 'Stopping bot', Utils.LogColors.FAIL)
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
                    r = MHandler.handle_message(update, lang)
                    # print('HANDLED_MSG: ' + str(r))
                    Utils.log_mess('HANDLED_MSG', str(r))
                    response = 'none'
                    for mess in r:
                        # print('MSG: ' + str(mess))
                        Utils.log_mess('MSG', str(mess))
                        if mess == 'NONE':
                            response = Utils.send_mess(Utils.get_chat_id(update), Utils.inte('stopbot', lang))
                            break
                        else:
                            response = Utils.send_mess(Utils.get_chat_id(update), mess[0], mess[1])
                    if response:
                        # print('RESPONSE: ' + str(response.json()))
                        Utils.log_mess('RESPONSE', str(response.json()), Utils.LogColors.RESPONSE)
                    else:
                        # print('STOPPING')
                        stop_bot()
                elif update.get('callback_query'):
                    callback_query = update.get('callback_query')
                    # print('CALLBACK: ' + str(callback_query))
                    Utils.log_mess('CALLBACK', 'Query ' + str(callback_query), Utils.LogColors.OKBLUE)
                    r = MHandler.handle_callback(update)
                    # print('CALLBACK: ' + str(r))
                    Utils.log_mess('CALLBACK', str(r), Utils.LogColors.OKBLUE)

                    # name = 'You'
                    # if callback_query.get('from').get('username'):
                    #     name = '@' + callback_query['from']['username']
                    # elif callback_query.get('from').get('first_name'):
                    #     name = callback_query.get('from').get('first_name')
                    # Utils.send_mess(callback_query['message']['chat']['id'], name + ' told me ' + callback_query['data'])
                update_id = Utils.last_update(Utils.get_updates_json(url))['update_id'] + 1
        except KeyboardInterrupt:
            stop_bot()
        except Exception as e:
            Utils.log_mess('ERROR', str(type(e)) + ' --> ' + str(e), Utils.LogColors.FAIL)
            Utils.log_mess('ERROR_READOUT', '\n' + Utils.LogColors.FAIL + Utils.list_to_lines(traceback.format_list(traceback.extract_tb(sys.exc_info()[2]))), Utils.LogColors.FAIL)
            # stop_bot()


if __name__ == '__main__':
    main()
