import requests
import bot_token

url = 'https://api.telegram.org/bot' + bot_token.t + '/'  # Your bot's token


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
        params = {'chat_id': chat, 'text': text, 'reply_markup': custom}
    print('SEND_MSG_PARAMS: ' + str(params))
    response = requests.post(url + 'sendMessage', data=params)
    return response


def send_callback(callbackId, params):
    p = {'callback_query_id': callbackId}
    p.update(params)
    print('SEND_CALLBACK: Sending callback')
    return requests.post(url + 'answerCallbackQuery', data=p)


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
    r = {'inline_keyboard': buttons}
    if custom is not None:
        r.update(custom)
    return r


def generate_poll(poll_id, options):
    r = '{"inline_keyboard": ['
    for option in options:
        r += '[{"text": "' + option + '", "callback_data": "' + str(poll_id) + ':::' + option + '"}]'
        if options.index(option) < (len(options)-1):
            r += ','
    r += ']}'
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


def get_test_keyboard():
    return '{"inline_keyboard": [[{"text": "A", "callback_data": "Poll1|-->|A"}, {"text": "B", "callback_data": "B"}]]}'
