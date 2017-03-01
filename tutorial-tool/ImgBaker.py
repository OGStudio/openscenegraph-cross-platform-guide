
from Item import *

IMG_EXT = "png"
TEXT_COLOR = "white"
TEXT_SIZE = "40"
CMD = (
    "convert {src} "
    "-fill {color} "
    "-pointsize {size} "
    "-gravity center "
    "-annotate 0 \"{text}\" "
    "{dst}"
    )

def imgFileName(type, id):
    return "{0}-{1:02d}.{2}".format(type, id, IMG_EXT)

class ImgBaker(object):
    def __init__(self):
        self.cmds = []
    def bake(self, background, items, dstDir):
        self.cmds = []
        i = 0
        for item in items:
            if (item.type == ITEM_TYPE_TEXT):
                fileName = imgFileName(ITEM_TYPE_TEXT, i)
                filePath = dstDir + fileName
                self.cmds.append(
                    CMD.format(
                        src = background,
                        color = TEXT_COLOR,
                        size = TEXT_SIZE,
                        text = item.content,
                        dst = filePath
                    )
                )
            i = i + 1
    def script(self):
        s = ""
        for cmd in self.cmds:
            s += cmd + "\n"
        return s

