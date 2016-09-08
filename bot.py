#!/usr/bin/python

import time, json, os, requests, urllib, subprocess
from slackbot.bot import *
import logging, sys, bot

msg_help = {}

def dump(obj):
    for attr in dir(obj):
        print "obj.%s = %s" % (attr, getattr(obj, attr))

def my_upload(message, fname):
    global config

    if ('name' in message.channel._body.keys()):
        chan = message.channel._body['name']
    else:
        chan = message.channel._body['user']
    r = requests.post('https://slack.com/api/files.upload',
                      files={'file': open(fname, 'rb')},
                      params={'token': config['token'],
                              'channels': chan,
                              'filename': fname})

def my_chan(message):
    global config
    if ('name' in message.channel._body.keys()):
        return (message.channel._body['name'] == config['group'])
    else:
        return (True)

def my_master(message):
    global config
    return (True)

def main():
    logging.basicConfig(stream=sys.stdout,level=logging.ERROR)
    b = Bot()
    print "run bot in #%s (my master is %s)" % (bot.config['group'], bot.config['master'])
    b.run()

if __name__ == "__main__":
    main()
                
