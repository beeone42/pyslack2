#!/usr/bin/python

import json, os, bot

with open("config.json") as json_data_file:
    bot.config = json.load(json_data_file)
    API_TOKEN = bot.config["token"]

DEFAULT_REPLY = "Sorry but I didn't understand you"
PLUGINS = ['help', 'cam', 'open', 'snap']
DEBUG = False
