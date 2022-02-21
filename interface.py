
import pyglet
from pyglet import shapes

width = 500
height = 500
from dataclasses import dataclass


class Grid():
    def __init__(self, width, height, maxRows, maxColumns):
        self.width = width
        self.height = height
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.rowThickness = height / maxRows
        self.columnThickness = width / maxColumns
        self.points = []
        for i in range(1, self.maxColumns):
            for j in range(1, self.maxRows):
                x = self.columnThickness * i
                y = self.rowThickness * j
                self.points.append((x,y))

myGrid = Grid(width, height, 5, 5)
print(myGrid.points)

#textEntry = pyglet.gui.widgets.TextEntry("text", 10, 10, 30)

class Interface(pyglet.window.Window):
    def __init__(self, width, height):
        super(Interface, self).__init__()

        self.label = pyglet.text.Label('Hello, world!')
        self.width = width
        self.height = height
        self.gridBatch = pyglet.graphics.Batch()
        self.grid = Grid(width, height, 5, 5)
        self.gridSize = len(self.grid.points)
        self.gridLines = []
        for i in range(self.gridSize):
            print(self.grid.points[i])


    def on_draw(self):

        self.clear()
        self.gridBatch.draw()
        self.label.draw()
        self.set_caption("Interface")

if __name__ == '__main__':

    window = Interface(width, height)
    #event_logger = pyglet.window.event.WindowEventLogger()
    #window.push_handlers(event_logger)
    pyglet.app.run()

