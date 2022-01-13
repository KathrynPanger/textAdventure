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
            [None, "Car", None, None],
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
Map.playerY = 2
Map.playerZ = 2
Map.theLocation = Map.layout[Map.playerZ][Map.playerY-1][Map.playerX]

def getLocation():
    return (Map.theLocation,[Map.playerZ, Map.playerY, Map.playerX])

def movePlayer(direction):
    if direction == "n":
        if Map.playerY-1 >= 0 and Map.layout[Map.playerZ][Map.playerY-1][Map.playerX] != None:
            Map.playerY -= 1
            Map.theLocation = Map.layout[Map.playerZ][Map.playerY-1][Map.playerX]

        else:
            print("You can't go that way")
            print(Map.layout[Map.playerZ][Map.playerY-1][Map.playerX])
