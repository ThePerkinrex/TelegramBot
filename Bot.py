import MessageHandler as MHandler
import Utils


url = "https://api.telegram.org/bot479189806:AAFgwI7drgzRoXTGnoCxgrFyfWcUxKP1Wlc/"


chat_id = Utils.get_chat_id(Utils.last_update(Utils.get_updates_json(url)))
Utils.send_mess(chat_id, 'Telegram Bot On')


def main():
    if Utils.last_update(Utils.get_updates_json(url)) is None:
        update_id = 1
    else:
        update_id = Utils.last_update(Utils.get_updates_json(url))['update_id']
    while True:
        update = Utils.last_update(Utils.get_updates_json(url, update_id))
        if update is not None:
            # Utils.send_mess(Utils.get_chat_id(update), MHandler.handleMessage(update))
            mess = MHandler.handleMessage(update)
            for message in mess:
                Utils.send_mess(Utils.get_chat_id(update), message)
            update_id = Utils.last_update(Utils.get_updates_json(url))['update_id'] + 1


if __name__ == '__main__':
    main()
