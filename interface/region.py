from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interface.tile import Tile
    from style import Style


class Region:
    def __init__ (self, name: str, style: Style,
                  activeBorders: list):
        self.name = name
        self.activeBorders = activeBorders
        self.style = style
        self.tiles = []
        self.background = None

    def addTile(self, tile: Tile):
        self.tiles.append(tile)