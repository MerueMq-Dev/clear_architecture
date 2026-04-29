import pure_robot as robot

class RobotAPI:
    def __init__(self):
        self._state = robot.RobotState(x=0, y=0, angle=0, state=robot.WATER)
        self._transfer = robot.transfer_to_cleaner

    def move(self, distance: int):
        self._state = robot.move(self._transfer, distance, self._state)

    def turn(self, angle: int):
        self._state = robot.turn(self._transfer, angle, self._state)

    def set_mode(self, mode: str):
        """Режим: 'water', 'soap', 'brush'"""
        self._state = robot.set_state(self._transfer, mode, self._state)

    def start(self):
        self._state = robot.start(self._transfer, self._state)

    def stop(self):
        self._state = robot.stop(self._transfer, self._state)

    def run_script(self, commands: list[str]):
        self._state = robot.make(self._transfer, commands, self._state)