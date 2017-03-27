
from Common import *
from Item import *

class YoutubeTimestampBaker(object):
    def __init__(self, mixLen):
        self.items = []
        self.mixLen = mixLen
    def bake(self, items):
        self.items = []
        timestamp = 0
        for item in items:
            if (item.type == ITEM_TYPE_TEXT):
                duration = int(item.duration)
                textTimeStamp = timestamp + int(duration / 2.0)
                minSecTimeStamp = timestampToMinSec(textTimeStamp)
                timestamp += duration - MIX_LEN
                self.items.append("* [ {0} ] {1} ".format(minSecTimeStamp, item.content))
            elif (item.type == ITEM_TYPE_VIDEO):
                startEnd = item.duration.split(":")
                start = int(startEnd[0])
                end = int(startEnd[1])
                timestamp += (end - start - MIX_LEN)
    def script(self):
        return "\n".join(self.items)

