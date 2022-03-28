import map
import command
import action
from items import Item, Category, Container

room_data = read_rooms("data/rooms.txt")

theLocation = map.playerLocation
print(theLocation)

barrel = Container(name = "treasure_chest",
                   printedName = "Treasure Chest",
                   is_open = False, is_lockable = True,
                   is_locked = True,
                   contents = [Item(name = 'necklace')],
                   capacity = 5)
print(theLocation.contents)
print(barrel.contents)
