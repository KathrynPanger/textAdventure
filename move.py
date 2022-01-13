class Map:
    pass

Map = Map()
Map.layout = {
        0: [
        ["Covered Hole", "Atrium","Torture Chamber"],
        [None, "Titan Hallway", None],
        [None, "Bottom of Pit", None]

        ],
        1: [
            ["Cramped Corner", "Breaker Box", None],
            ["Boiler Room", None, None],
            ["Corridor End", "Dark Corridor", "Bottom of Stairs"],
            ["Narrow Gap", None, None],
            ["Wet Corner", "Flooded Pit"]
        ],
        2: [
            [None, "car", None, None],
            ["Study", "Foyer", "Lounge" ],
            ["Library", "Main hall", "Dining Room"],
            ["Small Bathroom", "Short Hall", "Stair Landing"],
            ["Conservatory", "Ballroom", "Kitchen"]
        ],
        3: [
            ["Master Bathroom", "Laboratory", "Secret Room"],
            ["Master Bedroom", "Bloody Corridor", "Closet"],
            ["Upstairs Bathroom", "Dim Passage", "Top of Stairs"],
            ["Child's Bedroom", "Guest Bedroom", None],
            ]
        }
Map.playerX = 1
Map.playerY = 0
Map.playerZ = 2

def getLocation():
    return [Map.playerX, Map.playerY, Map.playerZ]

def movePlayer(direction):
    if direction == "n":
        if Map.playerY-1 >= 0 and Map.layout[Map.playerX, Map.playerY-1, Map.playerZ] != None:
            Map.playerY -= 1
        else:
            print("You can't go that way")
