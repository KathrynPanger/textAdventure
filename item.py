class Item:
    def __init__ (self, name):
        self.name =  name

    def __repr__(self):
        return self.name

class Container:
    def __init__(self, name, is_lockable = False, is_locked = False):
        self.name = name


    def fillWith(self, item: Item):
        self.contents.append(item)

    def lockWith(self, key):

