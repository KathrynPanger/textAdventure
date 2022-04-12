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
    batch: Batch = field(hash = False)
    lines: list[shapes.Line] = field(default_factory = list, init = False, hash = False)
    def __post_init__(self):
        line = shapes.Line(*self.ul, *self.ur, width=2,
                           batch=self.batch,
                           color=(255, 255, 255))
        self.lines.append(line)
        line = shapes.Line(self.ll.x, self.ll.y, self.lr.x, self.lr.y, width=2,
                           batch=self.batch,
                           color=(255, 255, 255))
        self.lines.append(line)

    def draw(self):
        pass



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
        self.circles = []
        for i in range(self.numberOfColumns + 1):
            for j in range(self.numberOfRows + 1):
                x = self.columnThickness * i
                y = self.rowThickness * j
                self.points.add(Point(x, y))
                self.circles.append(shapes.Circle(x, y, 10, batch=self.batch))
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

    def draw(self):
        for tile in self.tiles:
            tile.draw()


class Interface(pyglet.window.Window):
    def __init__(self, width, height, batches: list[Batch]):
        super(Interface, self).__init__()

        self.label = pyglet.text.Label('Hello, world!')
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
    window = Interface(width, height, batches=[lineBatch, gridBatch])
    # event_logger = pyglet.window.event.WindowEventLogger()
    # window.push_handlers(event_logger)

    myGrid = Grid(width, height, 5, 5, batch=gridBatch)
    myGrid.draw()
    pyglet.app.run()
