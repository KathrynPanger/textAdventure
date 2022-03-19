import pyglet
from pyglet import shapes
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

if __name__ == '__main__':
    width = 640
    height = 420
    lineBatch = Batch()
    circleBatch = Batch()
    window = Interface(width, height, batches = [lineBatch, circleBatch])
    event_logger = pyglet.window.event.WindowEventLogger()
    window.push_handlers(event_logger)

    line = shapes.Line(0,0,640,420, width = 2, batch = lineBatch, color = (255,255,255))

    pyglet.app.run()
