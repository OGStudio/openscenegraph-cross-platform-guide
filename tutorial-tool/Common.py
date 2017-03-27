
IMG_EXT = "png"

# Duration of text-to-video or video-to-text transition.
MIX_LEN = 1

def imgFileName(type, id):
    return "{0}-{1:02d}.{2}".format(type, id, IMG_EXT)

def timestampToMinSec(timestamp):
    minutes = int(timestamp / 60)
    seconds = int(timestamp - minutes * 60)
    res = "{0:02d}:{1:02d}".format(minutes, seconds)
    print("timestampToMinSec({0}): '{1}'".format(timestamp, res))
    return res
