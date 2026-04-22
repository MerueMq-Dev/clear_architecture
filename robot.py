import math
from enum import Enum

class CleaningType(Enum):
    WATER = "water"
    SOAP = "soap"
    BRUSH = "brush"

class Position:
    def __init__(self, x:float, y:float):
        self.x:float = x
        self.y:float = y

class Robot:
    current_position: Position = Position(0, 0)
    current_cleaning_type: CleaningType = CleaningType.WATER
    current_angle : int = 0
    is_working: bool = False

    def turn(self, angle: int) -> None:
        self.current_angle = (self.current_angle + angle) % 360
        print(f"ANGLE: {self.current_angle}")

    def move(self, distance:int) -> None:
        rad = math.radians(self.current_angle)
        self.current_position.x += distance * math.cos(rad)
        self.current_position.y += distance * math.cos(rad)
        print(f"POS: {self.current_position.x} {self.current_position.y} ")

    def set(self, cleaning_type: CleaningType = CleaningType.WATER) -> None:
        self.current_cleaning_type = cleaning_type
        print(f"STATE: {cleaning_type.value}")

    def start(self) -> None:
        self.is_working = True
        print(f"START WITH {self.current_cleaning_type.value}")

    def stop(self) -> None:
        self.is_working = False
        print(f"STOP")

def run_program(commands: list[str]) -> None:
    robot = Robot()

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
                cleaning_type = cleaning_map.get(parts[1], CleaningType.WATER)
                robot.set(cleaning_type)
            case "start":
                robot.start()
            case "stop":
                robot.stop()
            case _:
                print(f"Unknown command: {parts[0]}")