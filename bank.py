from slackbot.bot import listen_to
from bot import *
import re, requests, json

msg_help['balance'] = "*balance* <login> _# show user foodtruck balance_"
msg_help['ops'] = "*ops* <login> _# show user foodtruck operations_"
msg_help['credit']  = "*credit* <login> <amount>_# add amount to user foodtruck balance_"
msg_help['pay']     = "*pay* <login> <amount> _# remove amount from user foodtruck balance_"

@listen_to('^balance ([a-zA-Z0-9_-]+)$')
def balance(message, login):
    if (my_chan(message)):
        r = requests.get(config['bank_base'] + "balance.php?login=" + login + "&vendor=" + config['bank_vendor'] + "&key=" + config['bank_key'])
        j = json.loads(r.content)
        message.send(j['balance'])

@listen_to('^ops ([a-zA-Z0-9_-]+)$')
def ops(message, login):
    if (my_chan(message)):
        r = requests.get(config['bank_base'] + "ops.php?login=" + login + "&vendor=" + config['bank_vendor'] + "&key=" + config['bank_key'])
        message.send(r.content)

@listen_to('^credit ([a-zA-Z0-9_-]+) ([0-9.]+)$')
def credit(message, login, amount):
    if (my_chan(message)):
        r = requests.get(config['bank_base'] + "credit.php?login=" + login + "&amount=" + amount + "&vendor=" + config['bank_vendor'] + "&key=" + config['bank_key'])
        message.send(r.content)

@listen_to('^pay ([a-zA-Z0-9_-]+) ([0-9.]+)$')
def pay(message, login, amount):
    if (my_chan(message)):
        r = requests.get(config['bank_base'] + "pay.php?login=" + login + "&amount=" + amount + "&vendor=" + config['bank_vendor'] + "&key=" + config['bank_key'])
        message.send(r.content)

