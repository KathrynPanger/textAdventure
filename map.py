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
        self.data: dict[Location, Room] = {}
        for z, floor in data.items():
            #JSON items are string, make z-value an integer
            z = int(z)
            #Create room locations with x, y and z value matching map data.
            for y, row in enumerate(floor):
                for x, room in enumerate(row):
                    loc = Location(x,y,z)
            #Assign each location a room object
                    self.data[loc] = Room(room)
            #Set the properties of each room
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
playerLocation = map.data[Location(0,0,0)]
#print(map.data)