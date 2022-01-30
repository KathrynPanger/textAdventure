from map import Location, Map

import json

with open('mapData.json') as map_file:
    data = json.load(map_file)

map = Map(data)

#The Player's Location
playerLocation = Location(0,0,0)

