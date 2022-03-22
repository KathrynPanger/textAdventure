from typing import NamedTuple
from room import Room
import json


class Location(NamedTuple):
    x: int
    y: int
    z: int


class Map:
    def __init__(self, layout, roomData):
        self.layout: dict[Location, Room] = {}
        self.entities: dict[Location, entity] = {}
        self.roomData: dict[str, str] = roomData
        for z, floor in layout.items():
            # Create room locations with x, y and z value using layout data
            for y, row in enumerate(floor):
                for x, room in enumerate(row):
                    loc = Location(x,y,z)
            # Assign each location a room object using room data
                    description = roomData["description"]
                    exits = roomData["exits"]
                    contents = roomData["items"]
                    self.layout[loc] = Room(room, description, exits, contents)


    def __getitem__(self, location: Location):
        try:
            return self.layout[location]
        except KeyError:
            return None


# with open('data/mapData.json') as map_file:
#     data = json.load(map_file)
#
# map = Map(data)
#
# #The Player's Location
# playerLocation = map.layout[Location(0,0,0)]
# #print(map.data)