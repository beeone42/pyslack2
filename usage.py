from slackbot.bot import listen_to
from bot import *
import re, requests

msg_help['usage'] = "*usage* _# return number of people in the building_"

@listen_to('^usage$')
def usage(message):
    if (my_chan(message)):
        r = requests.get(config['usage_url'])
        message.send(str(r.content))
