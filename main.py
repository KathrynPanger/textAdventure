import map
import command
import action
from items import Item, Category, Container

theLocation = map.playerLocation
print(theLocation)

barrel = Container(name = "treasure_chest",
                   printedName = "Treasure Chest",
                   is_open = False, is_lockable = True,
                   is_locked = True,
                   contents = [Item(name = 'necklace')],
                   keyLocation = theLocation,
                   keyPrintedName = "Gold Key")
#barrel.modifyContainer(is_open = False, is_lockable = True, is_locked = True, contents = [Item("necklace",)], keyLocation = theLocation)
print(theLocation.contents)
print(barrel.contents)
#print(f"You found a {barrel:key}!")