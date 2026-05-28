import math

from either.robot_state import RobotState
from either.responses import MoveResponse, SetStateResponse, OK
from either.checks import check_position, check_resources


def move(dist):
    def inner(state, log):
        rads = state.angle * (math.pi / 180.0)
        raw_x = state.x + dist * math.cos(rads)
        raw_y = state.y + dist * math.sin(rads)

        new_x, new_y, response = check_position(raw_x, raw_y)
        new_state = RobotState(new_x, new_y, state.angle, state.state)
        new_log = log + [f'MOVE -> ({int(new_x)},{int(new_y)}) [{response}]']
        return new_state, new_log, response
    return inner


def turn(angle):
    def inner(state, log):
        new_state = RobotState(state.x, state.y, state.angle + angle, state.state)
        return new_state, log + [f'TURN -> {new_state.angle}'], OK
    return inner


def set_state(new_mode, resources):
    def inner(state, log):
        response = check_resources(new_mode, resources)
        if response != SetStateResponse.OK:
            # ресурса нет — режим не меняю и сразу возвращаю ошибку
            return state, log + [f'SET {new_mode} FAILED [{response}]'], response

        new_state = RobotState(state.x, state.y, state.angle, new_mode)
        return new_state, log + [f'SET -> mode {new_mode}'], response
    return inner


def start(state, log):
    return state, log + ['START'], OK


def stop(state, log):
    return state, log + ['STOP'], OK