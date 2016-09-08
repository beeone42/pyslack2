from slackbot.bot import listen_to
from bot import *
import re, os

msg_help['load'] = "*load* _# display load average_"

@listen_to('^load$')
def load(message):
    if (my_chan(message)):
        l = os.getloadavg()
        print "%.2f " * len(l) % tuple(l)
        message.send("%.2f " * len(l) % tuple(l))
