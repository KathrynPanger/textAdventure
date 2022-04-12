class Region():
    def __init__ (self, groupNumber: int, style: Style,
                  activeBorders: list, tiles: list, batch):
        self.groupNumber = groupNumber
        self.activeBorders = activeBorders
        self.style = style
        self.batch = batch
        self.tiles = tiles
        self.lines = [] # list[shapes.Line]
        self.background = None #rectangle of correct color
        for tile in self.tiles:
            ul = tile.ul
            ur = tile.ur
            ll = tile.ll
            lr = tile.lr
            width = ur - ul
            height = ul - ll
            borders = [[ul, ur], [ll, lr], [ul, ll], [ur, lr]]
            self.background = Rectangle(ul.x, ul.y, width, height,
                                   color=(self.style.backgroundColor), batch=self.batch,
                      group=background)
            for border in borders:
                line = shapes.Line(border[0], border[1],
                                   width = self.style.borderThickness,
                                   batch = self.batch,
                                   color = self.style.borderColor,
                                   group = foreground)
                self.lines.append(line)