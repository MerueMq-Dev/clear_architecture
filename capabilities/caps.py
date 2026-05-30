from capabilities.robot import RobotStatus, Mode
import capabilities.robot as robot

class BaseCaps:

    def __init__(self, state):
        self._state = state

    def info(self):

        return {
            'position': (
                self._state.x,
                self._state.y
            ),
            'angle': self._state.angle,
            'mode': self._state.mode.name,
            'resources': {
                k.name: v
                for k, v in self._state.resources.items()
            }
        }

class Idle:

    def __init__(self, state):
        self._state = state

    def move(self, dist):
        state = robot.move(
            self._state,
            dist
        )
        return build_caps(state)

    def turn(self, angle):
        state = robot.turn(
            self._state,
            angle
        )
        return build_caps(state)

    def start(self):
        state = robot.start(
            self._state
        )
        return build_caps(state)
    @property
    def water(self):

        if self._state.resources.get(
            Mode.WATER, 0
        ) <= 0:
            raise AttributeError

        def op():
            return build_caps(
                robot.set_mode(
                    self._state,
                    Mode.WATER
                )
            )

        return op

    @property
    def soap(self):

        if self._state.resources.get(
            Mode.SOAP, 0
        ) <= 0:
            raise AttributeError

        def op():
            return build_caps(
                robot.set_mode(
                    self._state,
                    Mode.SOAP
                )
            )

        return op

    @property
    def brush(self):

        if self._state.resources.get(
            Mode.BRUSH, 0
        ) <= 0:
            raise AttributeError

        def op():
            return build_caps(
                robot.set_mode(
                    self._state,
                    Mode.BRUSH
                )
            )

        return op

class Cleaning(BaseCaps):
    def turn(self, angle):
        state = robot.turn(self._state, angle)
        return build_caps(state)

    def stop(self):
        state = robot.stop(self._state)
        return build_caps(state)


class Stuck(BaseCaps):
    def turn(self, angle):
        state = robot.turn(self._state, angle)
        return build_caps(state)

def build_caps(state):

    if state.status == RobotStatus.IDLE:
        return Idle(state)

    if state.status == RobotStatus.CLEANING:
        return Cleaning(state)

    if state.status == RobotStatus.STUCK:
        return Stuck(state)

    raise RuntimeError("unknown status")
