
IMG_EXT = "png"

def imgFileName(type, id):
    return "{0}-{1:02d}.{2}".format(type, id, IMG_EXT)

