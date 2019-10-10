from slackbot.bot import respond_to
from slackbot.bot import listen_to
from bot import *
import re

msg_help['help'] = "*help* _# show this help_"

@respond_to('^help$')
@listen_to('^help$')
def help(message):
    if (my_chan(message)):
        c = msg_help.keys()
        c.sort()
        res = "Commands:"
        for i in c:
            res = res + "\n"
            res = res + msg_help[i]
        message.send(res)

