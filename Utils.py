import requests

url = "https://api.telegram.org/bot479189806:AAFgwI7drgzRoXTGnoCxgrFyfWcUxKP1Wlc/"


def get_updates_json(request, offset=None):
    if offset is None:
        response = requests.get(request + 'getUpdates')
        return response.json()
    response = requests.get(request + 'getUpdates?offset=' + str(offset))
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    if total_updates == -1:
        return None
    return results[total_updates]


def get_chat_id(update):
    if update is None:
        return 0;
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
