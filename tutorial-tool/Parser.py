
from Item import *

# Language keywords.
BACKGROUND = "bg "
TEXT = "t "
VIDEO = "v "

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
        if (ln.startswith(BACKGROUND)):
            self.parseBackground(ln)
        elif (ln.startswith(TEXT)):
            self.parseText(ln)
        elif (ln.startswith(VIDEO)):
            self.parseVideo(ln)
    def parseLines(self, lines):
        for ln in lines:
            self.parseLine(ln)
    def parseText(self, ln):
        durationText = ln.replace(TEXT, "")
        duration, text = durationText.split(" ", 1)
        self.items.append(Item("text", duration, text))
    def parseVideo(self, ln):
        durationVideo = ln.replace(VIDEO, "")
        duration, video = durationVideo.split(" ", 1)
        self.items.append(Item("video", duration, video))
    def printTree(self):
        print "Background: '{0}'".format(self.background)
        for item in self.items:
            print "Item. Type: '{0}' Duration: '{1}' Content: '{2}'".format(
                item.type,
                item.duration,
                item.content)

