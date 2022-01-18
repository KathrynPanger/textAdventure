from typing import NamedTuple
from room import Room
import json


"""
class Location:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Location(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))
"""


class Location(NamedTuple):
    x: int
    y: int
    z: int

"""
class Map:
    def __init__(self, data):
        self.data: dict[Location, str] = {}
        for z, floor in data.items():
            for y, row in enumerate(floor):
                for x, room in enumerate(row):
                    loc = Location(x,y,z)
                    self.data[loc] = room
                    """

class Map:
    def __init__(self, data):
        self.data: dict[Location, str] = {}
        for z, floor in data.items():
            for y, row in enumerate(floor):
                for x, room in enumerate(row):
                    loc = Location(x,y,z)
                    self.data[loc] = Room(room)
                    self.data[loc].set_properties()


    def __getitem__(self, location: Location):
        try:
            return self.data[location]
        except KeyError:
            return None


with open('mapData.json') as map_file:
    data = json.load(map_file)

map = Map(data)

#The Player's Location
playerLocation = Location(1,0,1)