import command.pure_robot as pr

# Паттерн Command для управления роботом.
# Базовый класс команды.
class Command:
    def execute(self, transfer, state):
        raise NotImplementedError


class Move(Command):
    def __init__(self, dist):
        self.dist = dist

    def execute(self, transfer, state):
        return pr.move(transfer, self.dist, state)


class Turn(Command):
    def __init__(self, angle):
        self.angle = angle

    def execute(self, transfer, state):
        return pr.turn(transfer, self.angle, state)


class SetState(Command):
    def __init__(self, mode):
        self.mode = mode

    def execute(self, transfer, state):
        return pr.set_state(transfer, self.mode, state)


class Start(Command):
    def execute(self, transfer, state):
        return pr.start(transfer, state)


class Stop(Command):
    def execute(self, transfer, state):
        return pr.stop(transfer, state)