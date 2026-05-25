import state_monad.pure_robot as pr
from state_monad.state import State


# Команды робота, завёрнутые в монаду состояния.
# Каждая команда двигает робота И дописывает строку в лог.

# режимы для удобной записи
WATER = pr.WATER
SOAP  = pr.SOAP
BRUSH = pr.BRUSH


def _lift(core_call):
    # Превращает вызов функции из pure_robot в шаг монады.
    def step(s):
        robot_state, log = s
        captured = []

        # transfer не печатает, а складывает сообщение в список
        def transfer(message):
            captured.append(message)

        new_robot_state = core_call(transfer, robot_state)
        return (captured, (new_robot_state, log + captured))

    return State(step)


def move(dist):
    return _lift(lambda transfer, rs: pr.move(transfer, dist, rs))


def turn(angle):
    return _lift(lambda transfer, rs: pr.turn(transfer, angle, rs))


def set_state(mode_name):
    return _lift(lambda transfer, rs: pr.set_state(transfer, mode_name, rs))


def start():
    return _lift(lambda transfer, rs: pr.start(transfer, rs))


def stop():
    return _lift(lambda transfer, rs: pr.stop(transfer, rs))