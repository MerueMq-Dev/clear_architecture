# implementations.py
from interfaces import IRobotTransfer, IRobotAPI
from robot import Robot, CleaningType

class ConsoleTransfer(IRobotTransfer):
    def send(self, message: str) -> None:
        print(message)

class RobotAPI(IRobotAPI):
    def __init__(self, robot: Robot, transfer: IRobotTransfer):
        robot.logger = TransferLogger(transfer)  # внедряем transfer через logger
        self._robot = robot

    def move(self, distance: int) -> None:
        self._robot.move(distance)

    def turn(self, angle: int) -> None:
        self._robot.turn(angle)

    def set_mode(self, mode: str) -> None:
        cleaning_map = {
            "water": CleaningType.WATER,
            "soap": CleaningType.SOAP,
            "brush": CleaningType.BRUSH,
        }
        self._robot.set(cleaning_map.get(mode, CleaningType.WATER))

    def start(self) -> None:
        self._robot.start()

    def stop(self) -> None:
        self._robot.stop()