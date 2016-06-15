#!/usr/bin/python

import time, json, os, requests, urllib, subprocess
from slackbot.bot import *
import logging, sys

msg_help = {}

def my_upload(message, fname):
    global config
    params = ["curl", "-s", "-o", "/dev/null",
              "-F", "file=@" + fname,
              "-F", "channels=#" + message.channel._body['name'].encode('ascii','ignore'),
              "-F", "token=" + config['token'].encode('ascii','ignore'),
              "https://slack.com/api/files.upload"]
    subprocess.call(params)

def my_chan(message):
    global config
    return (message.channel._body['name'] == config['group'])

def main():
    print "run"
    logging.basicConfig(stream=sys.stdout,level=logging.ERROR)
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
                
