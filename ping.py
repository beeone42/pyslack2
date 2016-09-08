from slackbot.bot import listen_to
from bot import *
import re, os

msg_help['ping'] = "*ping* _# pong_"

@listen_to('^ping$')
def ping(message):
    if (my_chan(message)):
        message.send("pong")
