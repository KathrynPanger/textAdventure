from dataclasses import dataclass, field
from pyglet.graphics import Batch
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interface.region import Region
    from interface.line import Line
    from interface.point import Point


@dataclass(frozen = True)
class Tile:
    ul: Point
    ur: Point
    ll: Point
    lr: Point
    rowNumber: int
    columnNumber: int
    region: Region
    batch: Batch = field(hash = False)
    lines: list[Line] = field(default_factory = list, init = False, hash = False)

    def addLine(self, line: Line):
        self.lines.append(line)