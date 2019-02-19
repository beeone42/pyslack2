from slackbot.bot import respond_to
from slackbot.bot import listen_to
from bot import *
import re
import subprocess

msg_help['card'] = "*card* [login] _# get the card of login_"
msg_help['card_year'] = "*card* [login] [year] _# get the card of login/year_"
msg_help['print'] = "*print* [login] _# print the card of login_"
msg_help['print_year'] = "*print* [login] [year] _# print the card of login/year_"

def card_get_pdf(message, c, year):
    if (year != ''):
        card_name = c + "-" + year + ".pdf"
    else:
        card_name = c + ".pdf"
    print("grab card " + card_name)
    try:
        urllib.urlretrieve(config['card_base'] + c + "&syear=" + str(year), 'cache/' + card_name)
    except Exception as inst:
        print("error grabbing card " + card_name)
        message.send("Error grabing card: " + card_name)
        print inst
        message.send(str(type(inst)))
        return

def card_send_pdf(message, c, year):
    if (year != ''):
        card_name = c + "-" + year + ".pdf"
    else:
        card_name = c + ".pdf"
    print("post card " + card_name)
    try:
        my_upload(message, 'cache/' + card_name)
    except Exception as inst:
        print("error sending card " + card_name)
        message.send("Error sending card: " + card_name)
        print inst
        message.send(str(type(inst)))

def card_print_pdf(message, c, year):
    if (year != ''):
        card_name = c + "-" + year + ".pdf"
    else:
        card_name = c + ".pdf"
    print("print card " + card_name)
    try:
        subprocess.call(['/usr/bin/lp', '-d', 'EVOLIS', '-o', 'media=card', '-o', 'orientation-requested=4', '-o', 'GRibbonType/Ribbon=RC_YMCKO', 'cache/' + card_name])
    except Exception as inst:
        print("error printing card " + card_name)
        message.send("Error printing card: " + card_name)
        print inst
        message.send(str(type(inst)))

@respond_to('^card ([a-zA-Z0-9_-]+)$')
@listen_to('^card ([a-zA-Z0-9_-]+)$')
def card_login(message, c):
    if (my_chan(message)):
        message.send('ok i send you %s' % c)
        card_get_pdf(message, c, '')
        card_send_pdf(message, c, '')

@respond_to('^card ([a-zA-Z0-9_-]+) ([0-9]+)$')
@listen_to('^card ([a-zA-Z0-9_-]+) ([0-9]+)$')
def card_login(message, c, year):
    if (my_chan(message)):
        message.send('ok i send you %s (%s)' % (c, year))
        card_get_pdf(message, c, year)
        card_send_pdf(message, c, year)

@respond_to('^print ([a-zA-Z0-9_-]+)$')
@listen_to('^print ([a-zA-Z0-9_-]+)$')
def print_login(message, c):
    if (my_chan(message)):
        message.send('ok i print you %s' % c)
        card_get_pdf(message, c, '')
        card_print_pdf(message, c, '')

@respond_to('^print ([a-zA-Z0-9_-]+) ([0-9]+)$')
@listen_to('^print ([a-zA-Z0-9_-]+) ([0-9]+)$')
def print_login(message, c, year):
    if (my_chan(message)):
        message.send('ok i print you %s (%s)' % (c, year))
        card_get_pdf(message, c, year)
        card_print_pdf(message, c, year)
