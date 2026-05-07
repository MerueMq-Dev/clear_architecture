import math
from enum import Enum
from .interfaces import IRobot


class CleaningType(Enum):
    WATER = "water"
    SOAP = "soap"
    BRUSH = "brush"


class Position:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y


class ConsoleLogger:
    def log(self, message: str) -> None:
        print(message)


class Robot(IRobot):
    def __init__(self, logger=None) -> None:
        self.position = Position()
        self.cleaning_type = CleaningType.WATER
        self.angle = 0
        self.is_working = False
        self.logger = logger or ConsoleLogger()

    def turn(self, degrees: int) -> None:
        self.angle = (self.angle + degrees) % 360
        self.logger.log(f"ANGLE: {self.angle}")

    def move(self, distance: float) -> None:
        rad = math.radians(self.angle)
        self.position.x += distance * math.cos(rad)
        self.position.y += distance * math.sin(rad)
        self.logger.log(f"POS: {self.position.x} {self.position.y}")

    def set(self, mode: str) -> None:
        cleaning_map = {
            "water": CleaningType.WATER,
            "soap": CleaningType.SOAP,
            "brush": CleaningType.BRUSH,
        }
        self.cleaning_type = cleaning_map.get(mode, CleaningType.WATER)
        self.logger.log(f"STATE: {self.cleaning_type.value}")

    def start(self) -> None:
        self.is_working = True
        self.logger.log(f"START WITH {self.cleaning_type.value}")

    def stop(self) -> None:
        self.is_working = False
        self.logger.log("STOP")