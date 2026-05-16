from functools import partial
import  functional_di_robot_2.pure_robot as pr

# Возвращает одну функцию dispatch(command, state),
# которая внутри сама решает, какую операцию ядра выполнить.
def make_dispatch(transfer):
    # Связываем зависимость transfer с функциями ядра.
    move      = partial(pr.move,      transfer)
    turn      = partial(pr.turn,      transfer)
    set_state = partial(pr.set_state, transfer)
    start     = partial(pr.start,     transfer)
    stop      = partial(pr.stop,      transfer)

    def dispatch(command, state):
        action, *args = command
        if action == 'move':
            return move(args[0], state)
        if action == 'turn':
            return turn(args[0], state)
        if action == 'set':
            return set_state(args[0], state)
        if action == 'start':
            return start(state)
        if action == 'stop':
            return stop(state)
        raise ValueError(f"unknown command: {action}")

    return dispatch