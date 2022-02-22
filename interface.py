
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
        for i in range(self.maxColumns + 1):
            for j in range(self.maxRows + 1):
                x = self.columnThickness * i
                y = self.rowThickness * j
                self.points.append((x,y))
        for i in range(len(self.points)):
            point = self.points[i]
            x1 = point[0]
            y1 = point[1]
            sameRowPoints = [item for item in self.points if
                             item[0] == x1]
            sameRowPoints.remove(point)
            for newPoint in sameRowPoints:
                x2 = newPoint[0]
                y2 = newPoint[1]
                if x1 == x2 and abs(y1 - y2) == self.rowThickness:
                    print(f'points: {point}, {newPoint}')

myGrid = Grid(width, height, 5, 5)
#print(myGrid.points)

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

