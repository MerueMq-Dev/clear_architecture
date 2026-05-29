from dataclasses import dataclass
from typing import Callable, Any


# ответы выполнения

@dataclass
class MoveResponse:
    distance: float
    ok: bool


@dataclass
class TurnResponse:
    angle: float
    ok: bool


@dataclass
class StateResponse:
    mode: int
    ok: bool


# узлы дерева

class Command:
    # Базовый узел AST. interpret() реализуют интерпретаторы, не сами узлы.
    pass


@dataclass
class Move(Command):
    distance: float
    next: Callable[[MoveResponse], Command]


@dataclass
class Turn(Command):
    angle: float
    next: Callable[[TurnResponse], Command]


@dataclass
class SetState(Command):
    mode: int
    next: Callable[[StateResponse], Command]


@dataclass
class Start(Command):
    next: Callable[[Any], Command]


class Stop(Command):
    # Терминальный узел — лист дерева. У него нет next.
    pass