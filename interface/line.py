from typing import NamedTuple, Optional

import pyglet
from pyglet.graphics import Batch

from interface.point import Point
from interface.region import Region
from interface.style import Style


class Line(NamedTuple):
    startPoint: Point
    endPoint: Point
    regions: list[Region]

    def makeLine(self, style: Style, batch: Batch) -> \
            Optional[pyglet.shapes.Line]:
        if len(self.regions) <= 1:
            return None
        return pyglet.shapes.Line(*self.startPoint, *self.endPoint,
                                  width=style.borderThickness,
                                  color=style.borderColor,
                                  batch=batch)
