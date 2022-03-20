import pyglet
from pyglet import shapes
from typing import NamedTuple
from dataclasses import dataclass, field

from pyglet.graphics import Batch


class Point(NamedTuple):
    x: float
    y: float


@dataclass(frozen = True)
class Tile:
    ul: Point
    ur: Point
    ll: Point
    lr: Point
    rowNumber: int
    columnNumber: int

    def draw(self):
        pass


@dataclass
class Style:
      borderColor: tuple(int)
      borderThickness: int
      backgroundColor: tuple(int)
      textColor: tuple(int)
      textSize: int
      textFont: str
      textAnchor: str


class Region():
    def __init__ (self, groupNumber: int, style: Style, activeBorders: list, tiles: list, batch):
        self.groupNumber = groupNumber
        self.activeBorders = activeBorders
        self.style = style
        self.batch = batch
        self.tiles = tiles
        self.lines = [] # list[shapes.Line]
        for tile in self.tiles:
            ul = tile.ul
            ur = tile.ur
            ll = tile.ll
            lr = tile.lr
            borders = [[ul, ur], [ll, lr], [ul, ll], [ur, lr]]
            for border in borders:
                line = shapes.Line(border[0], border[1],
                                   width=self.style.borderThickness,
                                   batch=self.batch,
                                   color=self.style.borderColor)
                self.lines.append(line)


class Grid():
    def __init__(self, width: int, height: int,
                 numberOfRows: int, numberOfColumns: int, batch: Batch):
        self.width = width
        self.height = height
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.rowThickness = height / numberOfRows
        self.columnThickness = width / numberOfColumns
        self.points = set()
        self.tiles = set()
        self.batch = batch
        #self.circles = []
        for i in range(self.numberOfColumns + 1):
            for j in range(self.numberOfRows + 1):
                x = self.columnThickness * i
                y = self.rowThickness * j
                self.points.add(Point(x, y))
                #self.circles.append(shapes.Circle(x, y, 10, batch=self.batch))
                if i == self.numberOfColumns or j == self.numberOfRows:
                    continue
                self.tiles.add(Tile(
                    ll = Point(x, y),
                    ul = Point(x, y + self.rowThickness),
                    lr = Point(x + self.columnThickness, y),
                    ur = Point(x + self.columnThickness, y + self.rowThickness),
                    batch = self.batch,
                    columnNumber = i,
                    rowNumber = j
                ))




class Interface(pyglet.window.Window):
    def __init__(self, width, height, batches: list[Batch]):
        super(Interface, self).__init__()

        self.label = pyglet.text.Label("")
        self.width = width
        self.height = height
        self.batches = batches

    def on_draw(self):
        self.clear()
        self.label.draw()
        for batch in self.batches:
            batch.draw()
        self.set_caption("Interface")

    def on_expose(self):
        pass

    # def on_mouse_motion(self, x, y, dx, dy):
    #     pass
    #     # print(x, y, dx, dy)


if __name__ == '__main__':
    width = 640
    height = 420
    lineBatch = Batch()
    gridBatch = Batch()
    myGrid = Grid(width, height, 5, 5, batch=gridBatch)
    window = Interface(width, height, batches=[gridBatch])
    # event_logger = pyglet.window.event.WindowEventLogger()
    # window.push_handlers(event_logger)



    pyglet.app.run()
