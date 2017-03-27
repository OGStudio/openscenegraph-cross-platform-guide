
ITEM_TYPE_TEXT = "text"
ITEM_TYPE_VIDEO = "video"

class Item(object):
    def __init__(self, type, duration, content):
        self.type = type
        self.duration = duration
        self.content = content
    def __str__(self):
        return "Item(type: '{0}' duration: '{1}' content: '{2}')".format(
            self.type,
            self.duration,
            self.content)
