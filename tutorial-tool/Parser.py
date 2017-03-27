
from Item import *

# Language keywords.
BACKGROUND = "background "
COMMENT = "#"
TEXT = "{0} ".format(ITEM_TYPE_TEXT)
VIDEO = "{0} ".format(ITEM_TYPE_VIDEO)

class Parser(object):
    def __init__(self):
        self.background = None
        self.items = []
    def parseBackground(self, ln):
        bg = ln.replace(BACKGROUND, "")
        bg = bg.strip()
        self.background = bg
    def parseLine(self, ln):
        sln = ln.strip()
        # Ignore comments.
        if (sln.startswith(COMMENT)):
            return
        # Parse real data.
        if (sln.startswith(BACKGROUND)):
            self.parseBackground(sln)
        elif (sln.startswith(TEXT)):
            self.parseText(sln)
        elif (sln.startswith(VIDEO)):
            self.parseVideo(sln)
    def parseLines(self, lines):
        for ln in lines:
            self.parseLine(ln)
    def parseText(self, ln):
        durationText = ln.replace(TEXT, "")
        duration, text = durationText.split(" ", 1)
        self.items.append(Item(ITEM_TYPE_TEXT, duration, text))
    def parseVideo(self, ln):
        durationVideo = ln.replace(VIDEO, "")
        duration, video = durationVideo.split(" ", 1)
        self.items.append(Item(ITEM_TYPE_VIDEO, duration, video))
    def printTree(self):
        print("Background: '{0}'".format(self.background))
        for item in self.items:
            print(item)

