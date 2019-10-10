#!/usr/bin/python

import json, os, bot

print "loading settings..."

with open("config.json") as json_data_file:
    bot.config = json.load(json_data_file)
    API_TOKEN = bot.config["token"]
    ERRORS_TO = bot.config["master"]

DEFAULT_REPLY = "Sorry but I didn't understand you"
PLUGINS = ['help', 'usage', 'ping', 'card', 'debug', 'porte']
DEBUG = True
