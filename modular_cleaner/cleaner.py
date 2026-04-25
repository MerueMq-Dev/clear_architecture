import math
from .states import CleaningState
from typing import Callable


class Cleaner:
    def __init__(self, transfer: Callable[[str], None]) -> None:
        self.x = 0.0
        self.y = 0.0
        self.angle = 0
        self.state = CleaningState.WATER
        self.transfer = transfer

    def move(self, dist: int) -> None:
        angle_rads = self.angle * (math.pi / 180.0)
        self.x += dist * math.cos(angle_rads)
        self.y += dist * math.sin(angle_rads)
        self.transfer(f'POS x:{self.x:.2f}, y:{self.y:.2f}')

    def turn(self, turn_angle: int) -> None:
        self.angle += turn_angle
        self.transfer(f'ANGLE {self.angle}')

    def set_state(self, new_state: CleaningState) -> None:
        self.state = new_state
        self.transfer(f'STATE {self.state.value}')

    def start(self) -> None:
        self.transfer(f'START WITH {self.state.value}')

    def stop(self) -> None:
        self.transfer('STOP')