from slackbot.bot import listen_to
from bot import *
import re

msg_help['snap'] = "*snap* _# grab snap from mac_"

@listen_to('^snap$')
def snap(message):
    if (my_chan(message)):
        try:
            os.system("./imagesnap -q cache/snap.jpg")
            my_upload(message, "cache/snap.jpg")
        except Exception as inst:
            print("error snap")
            message.send("error snap")
            print inst
            message.send(str(type(inst)))

