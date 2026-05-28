import math
from dataclasses import dataclass

from stream_processing.robot_state import RobotState, CleaningMode


# намерения
@dataclass
class MoveRequested:  distance: float
@dataclass
class TurnRequested:  angle: float
@dataclass
class ModeRequested:  mode: CleaningMode
@dataclass
class StartRequested: pass
@dataclass
class StopRequested:  pass


# факты
@dataclass
class RobotMoved:
    distance: float
    def apply(self, s):
        rads = s.angle * (math.pi / 180.0)
        return RobotState(s.x + self.distance * math.cos(rads),
                          s.y + self.distance * math.sin(rads),
                          s.angle, s.state)

@dataclass
class RobotTurned:
    angle: float
    def apply(self, s):
        return RobotState(s.x, s.y, s.angle + self.angle, s.state)

@dataclass
class ModeChanged:
    mode: CleaningMode
    def apply(self, s):
        return RobotState(s.x, s.y, s.angle, self.mode.value)

@dataclass
class Started:
    def apply(self, s): return s

@dataclass
class Stopped:
    def apply(self, s): return s