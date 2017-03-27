
from Common import *
from Item import *

# Command to convert to 25 fps:
# melt -verbose -profile atsc_720p_25 SRC -consumer avformat:DST vcodec=libx264

CMD = """
    melt -verbose \\
    -profile atsc_720p_{fps} \\
    {items} -consumer avformat:{dst}.{ext} vcodec={vcodec}
"""
CMD_IMG = "{img} out={len} -mix {mix_len} -mixer luma \\\n"
CMD_VID = "{vid} in={start} out={end} -mix {mix_len} -mixer luma \\\n"
EXT = "mp4"
FILE_NAME = "video"
FPS = 25
VCODEC = "libx264"

def frameSec(sec):
    return FPS * sec

class MLTBaker(object):
    def __init__(self, dstDir, mixLen):
        self.items = []
        self.dstDir = dstDir
        self.mixLen = mixLen
    def bake(self, items, videoDir):
        self.items = []
        i = 0
        for item in items:
            if (item.type == ITEM_TYPE_TEXT):
                fileName = imgFileName(ITEM_TYPE_TEXT, i)
                filePath = self.dstDir + fileName
                self.items.append(
                    CMD_IMG.format(
                        img = filePath,
                        len = frameSec(int(item.duration)),
                        mix_len = frameSec(self.mixLen)
                    )
                )
            elif (item.type == ITEM_TYPE_VIDEO):
                startEnd = item.duration.split(":")
                start = int(startEnd[0])
                end = int(startEnd[1])
                self.items.append(
                    CMD_VID.format(
                        vid = videoDir + item.content,
                        start = frameSec(start),
                        end = frameSec(end),
                        mix_len = frameSec(self.mixLen)
                    )
                )
            i = i + 1
    def script(self):
        itemsScript = " ".join(self.items)
        filePath = self.dstDir + FILE_NAME
        return CMD.format(
            fps = FPS,
            items = itemsScript,
            dst = filePath,
            ext = EXT,
            vcodec = VCODEC
        )

