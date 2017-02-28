
from Item import *

CMD_BAKE_IMG = "convert {0} -fill white -pointsize 40 -gravity center -annotate 0 '{1}' {2}"

def imgName(type, id):
    return "{0}-{1:03d}.png".format(type, id)

class Formatter(object):
    def __init__(self):
        self.bakeCmds = []
    def format(self, background, items):
        i = 0
        for item in items:
            i = i + 1
            if (item.type == ITEM_TYPE_TEXT):
                fileName = imgName(ITEM_TYPE_TEXT, i)
                cmd = CMD_BAKE_IMG.format(background, item.content, fileName)
                self.bakeCmds.append(cmd)
            elif (item.type == ITEM_TYPE_VIDEO):
                print "TODO: video type cmd"

