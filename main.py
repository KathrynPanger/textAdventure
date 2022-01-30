import map
import command
import action
from items import Item, Category, Container

theLocation = map.playerLocation
print(theLocation)

barrel = Container("barrel", is_locked = True, is_lockable = True)
#barrel.modifyContainer(is_open = False, is_lockable = True, is_locked = True, contents = [Item("necklace", Category.takeable)], keyLoc = theLocation)
print(theLocation.contents)
print(f"You found a {barrel:key}!")