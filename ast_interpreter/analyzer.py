from collections import Counter

from ast_interpreter.ast_nodes import (
    Command, Move, Turn, SetState, Start, Stop,
    MoveResponse, TurnResponse, StateResponse,
)


def analyze(program: Command) -> Counter:
    counter = Counter()
    node = program
    while not isinstance(node, Stop):
        counter[type(node).__name__] += 1

        if isinstance(node, Move):
            node = node.next(MoveResponse(distance=node.distance, ok=True))
        elif isinstance(node, Turn):
            node = node.next(TurnResponse(angle=node.angle, ok=True))
        elif isinstance(node, SetState):
            node = node.next(StateResponse(mode=node.mode, ok=True))
        elif isinstance(node, Start):
            node = node.next(None)
        else:
            break

    counter["Stop"] += 1
    return counter