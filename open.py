from slackbot.bot import listen_to
from bot import *
import re, requests

msg_help['open'] = "*open* [door_name] _# without arg show door list, with arg open door_"

def dump(obj):
    for attr in dir(obj):
        print "obj.%s = %s" % (attr, getattr(obj, attr))

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

@listen_to('^open ([a-zA-Z0-9-]+)$')
def open_door(message, door):
    if (my_chan(message)):
        r = requests.get(config['open'][door])
        message.send(r.content)
