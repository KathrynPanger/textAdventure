from pyglet.graphics import Batch
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interface.line import Line
    from interface.point import Point
    from interface.region import Region
    from interface.tile import Tile


class Grid():
    def __init__(self, width: int, height: int,
                 numberOfRows: int, numberOfColumns: int,
                 regions: dict[tuple[int,int], Region],
                 batch: Batch):
        self.width = width
        self.height = height
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.rowThickness = height / numberOfRows
        self.columnThickness = width / numberOfColumns
        self.points: set[Point] = set()
        self.lines: dict[tuple[Point, Point], Line] = {}
        self.tiles: dict[tuple[int, int], Tile] = {}
        self.regions = regions
        self.batch = batch
        for i in range(self.numberOfColumns + 1):
            for j in range(self.numberOfRows + 1):
                x = self.columnThickness * i
                y = self.rowThickness * j
                self.points.add(Point(x, y))
                if i == self.numberOfColumns or j == self.numberOfRows:
                    continue
                tile = Tile(
                    ll = Point(x, y),
                    ul = Point(x, y + self.rowThickness),
                    lr = Point(x + self.columnThickness, y),
                    ur = Point(x + self.columnThickness, y + self.rowThickness),
                    columnNumber = i,
                    rowNumber = j,
                    region = regions[(i,j)]
                )
                self.tiles[(i, j)] = tile
                tile.region.addTile(tile)
                keys = [tuple(sorted(tile.ll, tile.ul)),
                        tuple(sorted(tile.ll, tile.lr)),
                        tuple(sorted(tile.ur, tile.ul)),
                        tuple(sorted(tile.ur, tile.lr))]
                for key in keys:
                    if key not in self.lines:
                        self.lines[key] = Line(*key, [tile.region])
                    elif tile.region not in self.lines[key].regions:
                        self.lines[key].regions.append(tile.region)

