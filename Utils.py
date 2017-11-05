import requests
import bot_token
import re

url = 'https://api.telegram.org/bot' + bot_token.t + '/'  # Your bot's token
maxlen = 20
msglangfile = 'lang/msg.lang'


def r_align(n, t):
    if len(t) >= n:
        return t
    else:
        while len(t) < n:
            t = ' ' + t
        return t


def list_to_lines(l):
    r = ''
    for item in l:
        r += item + '\n'
    return r


class LogColors:
    HEADER = '\033[95m'  # MSG RELATED
    OKBLUE = '\033[94m'  # UPDATE & CALLBACK RELATED
    OKGREEN = '\033[92m'  # POLLS RELATED
    RESPONSE = '\033[1;36m'  # RESPONSE RELATED
    LANG = '\033[1;34m'  # TRANSLATION
    WARNING = '\033[93m'  # WARNINGS
    FAIL = '\033[91m'  # ERRORS & END
    SETUP = '\033[32m'  # SETUP
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log_mess(type_txt, text, typec=LogColors.HEADER):
    print(typec + r_align(maxlen, type_txt) + ': ' + LogColors.ENDC + text + LogColors.ENDC)


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
    # print('SEND_MSG_PARAMS: ' + str(params))
    log_mess('SEND_MSG_PARAMS', str(params))
    response = requests.post(url + 'sendMessage', data=params)
    return response


def send_callback(callbackId, params):
    p = {'callback_query_id': callbackId}
    p.update(params)
    # print('SEND_CALLBACK: Sending callback')
    log_mess('CALLBACK', 'Sending callback', LogColors.OKBLUE)
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
    options.reverse()
    r = '{"inline_keyboard": ['
    for option in options:
        r += '[{"text": "' + option + '", "callback_data": "' + str(poll_id) + ':::' + option + '"}]'
        if options.index(option) < (len(options)-1):
            r += ','
    r += ']}'
    # print(r)
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


def inte(codename, lang):
    log_mess('LANG', 'Asked for ' + codename + '.' + lang, LogColors.LANG)
    regex = '\\b' + codename + '.' + lang + ' = (.*)\n'
    f = open(msglangfile)
    langf = f.read()
    f.close()
    reg = re.search(regex, langf)
    if reg:
        log_mess('LANG', codename + '.' + lang + ' --> ' + reg.group(1), LogColors.LANG)
        return reg.group(1)
    else:
        regex = codename + '.en-US = (.*)\n'
        reg = re.search(regex, langf)
        if reg:
            log_mess('LANG', codename + '.en-US --> ' + reg.group(1), LogColors.LANG)
            return reg.group(1)
        else:
            log_mess('LANG', codename + '.' + lang, LogColors.LANG)
            return codename + '.' + lang
