from dataclasses import dataclass, field


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