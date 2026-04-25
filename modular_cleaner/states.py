from enum import Enum


class CleaningState(Enum):
    WATER = 'water'
    SOAP = 'soap'
    BRUSH = 'brush'


def parse(name: str) -> CleaningState:
    try:
        return CleaningState(name)
    except ValueError:
        return CleaningState.WATER