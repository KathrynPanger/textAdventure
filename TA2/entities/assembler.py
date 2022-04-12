from util import read_rooms
import json
from map import Map

roomData = read_rooms("../data/rooms.txt")
layoutJson = open("../data/mapData.json")
layoutJson = json.load(layoutJson)
map = Map(layoutJson, roomData)

