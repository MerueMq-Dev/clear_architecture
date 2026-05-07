from .interfaces import IRobot, IRobotAPI


class RobotAPI(IRobotAPI):
    def __init__(self, robot: IRobot) -> None:
        self._robot = robot

    def move(self, distance: int) -> None:
        self._robot.move(distance)

    def turn(self, angle: int) -> None:
        self._robot.turn(angle)

    def set_mode(self, mode: str) -> None:
        self._robot.set(mode)

    def start(self) -> None:
        self._robot.start()

    def stop(self) -> None:
        self._robot.stop()