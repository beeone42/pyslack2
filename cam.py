from slackbot.bot import respond_to
from slackbot.bot import listen_to
from bot import *
import re

msg_help['cam'] = "*cam* [cam_name] _# without arg show cam list, with arg upload cam pic_"

@respond_to('^cam$')
@listen_to('^cam$')
def cam(message):
    if (my_chan(message)):
        k = config['cams'].keys()
        k.sort()
        res = "Cameras:"
        for i in k:
            res = res + "\n"
            res = res + "*" + i + "* : "
            cams = config['cams'][i]
            res = res + "_" + ",".join(cams) + "_"
        message.send(res)

def cam_get_pic(message, c):
    cam_name = c + ".jpg"
    print("grab cam " + cam_name)
    try:
        urllib.urlretrieve(config['cam_base'] + cam_name, 'cache/' + cam_name)
    except Exception as inst:
        print("error grabbing cam " + cam_name)
        message.send("Error grabing cam: " + cam_name)
        print inst
        message.send(str(type(inst)))
        return
    try:
        print("post cam " + cam_name)
        my_upload(message, 'cache/' + cam_name)
    except Exception as inst:
        print("error sending cam " + cam_name)
        message.send("Error sending cam: " + cam_name)
        print inst
        message.send(str(type(inst)))

@respond_to('^cam ([a-zA-Z0-9-]+)$')
@listen_to('^cam ([a-zA-Z0-9-]+)$')
def cam_pic(message, c):
    if (my_chan(message)):
        message.send('ok i send you %s' % c)
        if (len(config['cams']) > 0) and (c in config['cams'].keys()):
            message.send('%d cams to send' % len(config['cams'][c]))
            for i in config['cams'][c]:
                cam_get_pic(message, i)
        else:
            cam_get_pic(message, c)
