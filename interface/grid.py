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