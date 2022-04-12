import json
import sys
from util import read_rooms
sys.path.insert(0, '../entities')
from map import Map, Location

roomData = read_rooms("../data/rooms.txt")
layoutJson = open("../data/mapData.json")
layoutJson = json.load(layoutJson)
map = Map(layoutJson, roomData)
playerLocation = map.layout[Location(0,0,0)]
print(playerLocation.exits)