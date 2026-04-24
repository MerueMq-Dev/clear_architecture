import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Protocol


class CleaningType(Enum):
    WATER = "water"
    SOAP = "soap"
    BRUSH = "brush"


@dataclass
class Position:
    x: float = 0.0
    y: float = 0.0


class Logger(Protocol):
    def log(self, message: str) -> None: ...


class ConsoleLogger:
    def log(self, message: str) -> None:
        print(message)


@dataclass
class Robot:
    position: Position = field(default_factory=Position)
    cleaning_type: CleaningType = CleaningType.WATER
    angle: int = 0
    is_working: bool = False
    logger: Logger = field(default_factory=ConsoleLogger)

    def turn(self, degrees: int) -> None:
        self.angle = (self.angle + degrees) % 360
        self.logger.log(f"ANGLE: {self.angle}")

    def move(self, distance: float) -> None:
        rad = math.radians(self.angle)
        self.position.x += distance * math.cos(rad)
        self.position.y += distance * math.sin(rad)
        self.logger.log(f"POS: {self.position.x} {self.position.y}")

    def set(self, cleaning_type: CleaningType = CleaningType.WATER) -> None:
        self.cleaning_type = cleaning_type
        self.logger.log(f"STATE: {cleaning_type.value}")

    def start(self) -> None:
        self.is_working = True
        self.logger.log(f"START WITH {self.cleaning_type.value}")

    def stop(self) -> None:
        self.is_working = False
        self.logger.log("STOP")


def run_program(commands: list[str], logger: Logger | None = None) -> None:
    robot = Robot(logger=logger) if logger else Robot()

    cleaning_map = {
        "water": CleaningType.WATER,
        "soap": CleaningType.SOAP,
        "brush": CleaningType.BRUSH,
    }

    for command in commands:
        parts = command.strip().split()
        match parts[0]:
            case "move":
                robot.move(int(parts[1]))
            case "turn":
                robot.turn(int(parts[1]))
            case "set":
                robot.set(cleaning_map.get(parts[1], CleaningType.WATER))
            case "start":
                robot.start()
            case "stop":
                robot.stop()
            case _:
                robot.logger.log(f"Unknown command: {parts[0]}")