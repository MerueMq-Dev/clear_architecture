from __future__ import annotations
from dataclasses import dataclass, replace, field
from enum import Enum
from typing import Callable, Tuple
import math


class CleaningMode(Enum):
    WATER = 1
    SOAP  = 2
    BRUSH = 3


Transfer = Callable[[Tuple], None]


@dataclass(frozen=True)
class Cleaner:
    transfer: Transfer
    x: float = 0.0
    y: float = 0.0
    angle: float = 0.0
    mode: CleaningMode = CleaningMode.WATER

    # --- операции: возвращают НОВОГО Cleaner'а ---

    def move(self, dist: float) -> Cleaner:
        rads = self.angle * (math.pi / 180.0)
        new_x = self.x + dist * math.cos(rads)
        new_y = self.y + dist * math.sin(rads)
        self.transfer(('POS', new_x, new_y))
        return replace(self, x=new_x, y=new_y)

    def turn(self, turn_angle: float) -> Cleaner:
        new_angle = self.angle + turn_angle
        self.transfer(('ANGLE', new_angle))
        return replace(self, angle=new_angle)

    def set_mode(self, mode: CleaningMode) -> Cleaner:
        self.transfer(('STATE', mode.name))
        return replace(self, mode=mode)

    def start(self) -> Cleaner:
        self.transfer(('START WITH', self.mode.name))
        return self

    def stop(self) -> Cleaner:
        self.transfer(('STOP',))
        return self