from slackbot.bot import listen_to
from bot import *
import re, requests, json

msg_help['porte-pull']   = "*porte-pull* _# git pull porte42/_"
msg_help['porte-reboot'] = "*porte-reboot* _# reboot porte42/_"

@listen_to('^porte-pull$')
def porte_pull(message):
    if (my_chan(message)):
        r = requests.get(config['porte_base'] + config['porte_key'] + "/pull")
        message.send(r.content)

@listen_to('^porte-reboot$')
def porte_pull(message):
    if (my_chan(message)):
        r = requests.get(config['porte_base'] + config['porte_key'] + "/reboot")
        message.send(r.content)

