# TelegramBot

This is a python based telegram bot which at the moment can create polls

## How does it work

It accepts this commands for creating polls (They're consecutive)
```
>> Create a poll
>> The question is ¿A or B? 
>> A, B
```
After this sequence of commands it will have created a poll with the question ¿A or B? and the options A and B.
You can end a poll by saying:
```
End the poll #
```
`#` being the id of the poll (When it creates it it will say it)

## How do I run it

You need to create a file named `bot_token.py` where you need to add your bot's token in the format:
```python
t = 'botToken'
```

Also you'll need to install the requests python module. You can do this through pip for example
```bash
pip install requests
``` 
or if you need permissions 
```bash
sudo pip install requests
```
This package is located [here](https://pypi.python.org/pypi/requests/).

After all that you only need to run it through python version 3
```bash
python3 installdir/Bot.py lang
```
being `python3` your python version 3 installation, `installdir` the local directory for this repository and `lang` the language of the bot.
Currently, the language can be `en-US` for english and `es-ES` for spanish. The spanish commands can be found [here](docs/ESP_Commands.md).

**And you're done and the bot is running** :+1: :+1:
