import pyglet
from pyglet import shapes
from typing import NamedTuple
from dataclasses import dataclass, field
from pyglet.graphics import Batch


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
