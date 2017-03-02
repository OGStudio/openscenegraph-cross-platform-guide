
from Common import *
from Item import *

TEXT_COLOR = "white"
TEXT_SIZE = "40"
TEXT_OFFSET= "+0+100"
CMD = (
    "convert {src} "
    "-fill {color} "
    "-pointsize {size} "
    "-gravity center "
    "-annotate {offset} \"{text}\" "
    "{dst}"
    )

class ImgBaker(object):
    def __init__(self):
        self.cmds = []
    def bake(self, background, items, dstDir, fileInDir):
        self.cmds = []
        i = 0
        for item in items:
            if (item.type == ITEM_TYPE_TEXT):
                fileName = imgFileName(ITEM_TYPE_TEXT, i)
                filePath = dstDir + fileName
                self.cmds.append(
                    CMD.format(
                        src = fileInDir + background,
                        color = TEXT_COLOR,
                        size = TEXT_SIZE,
                        offset = TEXT_OFFSET,
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

