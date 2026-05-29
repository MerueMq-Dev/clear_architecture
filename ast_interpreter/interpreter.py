import math
from collections import namedtuple

from ast_interpreter.ast_nodes import (
    Command, Move, Turn, SetState, Start, Stop,
    MoveResponse, TurnResponse, StateResponse,
)


RobotState = namedtuple("RobotState", "x y angle mode")

WATER, SOAP, BRUSH = 1, 2, 3
FIELD_MIN, FIELD_MAX = 0, 100


class RealInterpreter:
    def __init__(self):
        self.state = RobotState(0.0, 0.0, 0.0, WATER)
        self.log = []

    def run(self, program: Command):
        node = program
        while not isinstance(node, Stop):
            node = self._step(node)
        self.log.append("STOP")

    def _step(self, node: Command) -> Command:
        if isinstance(node, Move):
            response = self._do_move(node.distance)
            return node.next(response)

        if isinstance(node, Turn):
            response = self._do_turn(node.angle)
            return node.next(response)

        if isinstance(node, SetState):
            response = self._do_set_state(node.mode)
            return node.next(response)

        if isinstance(node, Start):
            self.log.append("START")
            return node.next(None)

        raise ValueError(f"Unknown node: {node}")

    # действия
    def _do_move(self, dist):
        rads = self.state.angle * (math.pi / 180.0)
        raw_x = self.state.x + dist * math.cos(rads)
        raw_y = self.state.y + dist * math.sin(rads)

        cx = max(FIELD_MIN, min(FIELD_MAX, raw_x))
        cy = max(FIELD_MIN, min(FIELD_MAX, raw_y))
        hit = (cx, cy) != (raw_x, raw_y)

        self.state = self.state._replace(x=cx, y=cy)
        actual = math.hypot(cx - (self.state.x - (cx - cx)), 0)  # неважно для лога
        if hit:
            self.log.append(f"MOVE -> ({int(cx)},{int(cy)}) [BARRIER]")
        else:
            self.log.append(f"MOVE -> ({int(cx)},{int(cy)})")
        return MoveResponse(distance=dist, ok=not hit)

    def _do_turn(self, angle):
        new_angle = self.state.angle + angle
        self.state = self.state._replace(angle=new_angle)
        self.log.append(f"TURN -> {new_angle}")
        return TurnResponse(angle=new_angle, ok=True)

    def _do_set_state(self, mode):
        # для примера: режим SOAP всегда успешен, WATER -- мог бы и упасть
        self.state = self.state._replace(mode=mode)
        self.log.append(f"SET -> mode {mode}")
        return StateResponse(mode=mode, ok=True)