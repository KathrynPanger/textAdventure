from dataclasses import dataclass
from enum import Enum, auto
from room import Room
from typing import Optional

class Category(Enum):
    container = auto()
    key = auto()
    takeable = auto()
    scenery = auto()

@dataclass
class Item:
    name: str
    printedName: Optional[str] = None,
    sounds: Optional[Sound] = None

    def __post_init__(self):
        if self.printedName is None:
            self.printedName = self.name

    def __str__(self):
        return self.printedName

    #def __format__(self, format_spec: str):
    #    if format_spec == "n":
    #        return str(self)

class Container(Item):
    def __init__(self,
                 name: str,
                 printedName: Optional[str] = None,
                 contents: Optional[list] = None,
                 is_open: Optional[bool] = None,
                 is_lockable: Optional[bool] = None,
                 is_locked: Optional[bool] = None,
                 keyLocation:  Optional[Room] = None,
                 keyPrintedName: Optional[str] = None
                 ):
        super().__init__(name, printedName)
        self.keyPrintedName = keyPrintedName
        self.contents = contents
        if is_locked:
            assert not is_open
            assert is_lockable
            self.is_lockable = True
            self.is_locked = True
            self.key = Item(name = f"{self.name}_key", printedName = self.keyPrintedName)
            keyLocation.contents.append(self.key)

    def __format__(self, format_spec: str):
        if format_spec == "key":
            return str(self.key)
        return super().__format__(format_spec)


class Supporter(Item):
    def __init__(self,
                 name: str,
                 printedName: Optional[str] = None,
                 contents: Optional[list] = None,
                 ):
        super().__init__(name, printedName)
        self.contents = contents


class Dresser(Container, Supporter):
    pass
