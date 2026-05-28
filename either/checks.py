from either.responses import MoveResponse, SetStateResponse
from either.robot_state import WATER, SOAP

# Поле — прямоугольник 0..100 по обеим осям.
def check_position(x, y):
    cx = max(0, min(100, x))
    cy = max(0, min(100, y))
    if cx == x and cy == y:
        return cx, cy, MoveResponse.OK
    return cx, cy, MoveResponse.BARRIER

# Хватит ли ресурса на выбранный режим.
def check_resources(new_mode, resources):
    if new_mode == WATER and resources['water'] <= 0:
        return SetStateResponse.NO_WATER
    if new_mode == SOAP and resources['soap'] <= 0:
        return SetStateResponse.NO_SOAP
    return SetStateResponse.OK