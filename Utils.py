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


def send_mess(chat, text, custom=None):
    params = {'chat_id': chat, 'text': text}
    if custom is not None:
        params['reply_markup'] = custom
    response = requests.post(url + 'sendMessage', data=params)
    return response


"""
get_custom_keyboard(buttons, custom=None):
buttons: A list of rows represented by lists with keyboard_button dicts in the form of
[[A1,A2,A3], # Row 1
 [B1,B2,B3], # Row 2
 [C1,C2,C3]] # Row 3
 
Optionals:
custom ==> A dict with custom options
"""


def get_custom_keyboard(buttons, custom=None):
    r = {'keyboard': buttons}
    if custom is not None:
        r.update(custom)
    return r


"""
get_custom_button(text, custom=None):
text: the text of the button

Optionals:
custom ==> A dict with custom options
"""


def get_custom_button(text, custom=None):
    r = {'text': text}
    if custom is not None:
        r.update(custom)

    return r
