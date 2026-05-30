from dataclasses import dataclass, replace
from enum import Enum
from typing import Callable
import math


class Mode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3


class RobotStatus(Enum):
    IDLE = 1
    CLEANING = 2
    STUCK = 3


@dataclass(frozen=True)
class RobotState:
    x: float
    y: float
    angle: float

    mode: Mode
    status: RobotStatus

    resources: dict

    transfer: Callable


FIELD_MIN = 0.0
FIELD_MAX = 100.0


def create_state(transfer, resources=None):
    if resources is None:
        resources = {
            Mode.WATER: 2,
            Mode.SOAP: 1,
            Mode.BRUSH: 999
        }

    return RobotState(
        x=0.0,
        y=0.0,
        angle=0.0,
        mode=Mode.WATER,
        status=RobotStatus.IDLE,
        resources=resources,
        transfer=transfer
    )


def move(state: RobotState, dist: float) -> RobotState:
    rads = state.angle * math.pi / 180.0

    raw_x = state.x + dist * math.cos(rads)
    raw_y = state.y + dist * math.sin(rads)

    x = max(FIELD_MIN, min(FIELD_MAX, raw_x))
    y = max(FIELD_MIN, min(FIELD_MAX, raw_y))

    hit = (x, y) != (raw_x, raw_y)

    state.transfer(
        ('POS', x, y, '[BARRIER]' if hit else '')
    )

    return replace(
        state,
        x=x,
        y=y,
        status=RobotStatus.STUCK if hit else state.status
    )


def turn(state: RobotState, angle: float) -> RobotState:
    new_state = replace(
        state,
        angle=state.angle + angle
    )

    state.transfer(('ANGLE', new_state.angle))

    if state.status == RobotStatus.STUCK:
        new_state = replace(
            new_state,
            status=RobotStatus.IDLE
        )

    return new_state


def set_mode(state: RobotState, mode: Mode) -> RobotState:
    state.transfer(('SET', mode.name))

    return replace(
        state,
        mode=mode
    )


def start(state: RobotState) -> RobotState:
    state.transfer(
        ('START WITH', state.mode.name)
    )

    return replace(
        state,
        status=RobotStatus.CLEANING
    )


def stop(state: RobotState) -> RobotState:

    resources = dict(state.resources)

    resources[state.mode] = max(
        0,
        resources.get(state.mode, 0) - 1
    )

    state.transfer(('STOP',))

    return replace(
        state,
        status=RobotStatus.IDLE,
        resources=resources
    )