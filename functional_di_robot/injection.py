from functools import partial
import functional_di_robot.pure_robot as pr

# Возвращает функции ядра с уже впрыснутой зависимостью.
def inject(transfer):
    return {
        'move':      partial(pr.move,      transfer),
        'turn':      partial(pr.turn,      transfer),
        'set_state': partial(pr.set_state, transfer),
        'start':     partial(pr.start,     transfer),
        'stop':      partial(pr.stop,      transfer),
    }