from slackbot.bot import respond_to
from slackbot.bot import listen_to
from bot import *
import re, requests

msg_help['open'] = "*open* [door_name] _# without arg show door list, with arg open door_"

@respond_to('^open$')
@listen_to('^open$')
def open(message):
    if (my_chan(message)):
        k = config['open'].keys()
        k.sort()
        res = "Doors:"
        for i in k:
            res = res + "\n"
            res = res + i
        message.send(res)

@respond_to('^open ([a-zA-Z0-9-]+)$')
@listen_to('^open ([a-zA-Z0-9-]+)$')
def open_door(message, door):
    if (my_chan(message)):
        r = requests.get(config['open'][door])
        message.send(r.content)
