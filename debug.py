from slackbot.bot import respond_to
from slackbot.bot import listen_to
from bot import *
import re, os

msg_help['debug'] = "*debug* _# just debug_"

@respond_to('^debug$')
@listen_to('^debug$')
def debug(message):
    print "debug"
    if (my_chan(message)):
        message.send("debug")

@respond_to('^debug ([a-zA-Z0-9_-]+)$')
@listen_to('^debug ([a-zA-Z0-9_-]+)$')
def debug(message, p):
    print "debug: %s" % p
    if (my_chan(message)):
        message.send("debug: %s" % p)
