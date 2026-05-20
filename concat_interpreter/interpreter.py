"""
Конкатенативный интерпретатор для команд робота.
Программа — это строка токенов, разделённых пробелами.
Состояние робота всегда лежит на дне стека и обновляется на месте.
"""
from functools import partial
import  concat_interpreter.pure_robot as pr


def make_interpreter(transfer):
    # Связываем зависимость transfer с операциями ядра.
    move      = partial(pr.move,      transfer)
    turn      = partial(pr.turn,      transfer)
    set_state = partial(pr.set_state, transfer)
    start     = partial(pr.start,     transfer)
    stop      = partial(pr.stop,      transfer)

    # Словарь операций. Каждая операция работает со стеком:
    # снимает свои аргументы, кладёт обновлённое состояние.
    def op_move(stack):
        dist = stack.pop()
        state = stack.pop()
        stack.append(move(dist, state))

    def op_turn(stack):
        angle = stack.pop()
        state = stack.pop()
        stack.append(turn(angle, state))

    def op_set(stack):
        mode = stack.pop()
        state = stack.pop()
        stack.append(set_state(mode, state))

    def op_start(stack):
        state = stack.pop()
        stack.append(start(state))

    def op_stop(stack):
        state = stack.pop()
        stack.append(stop(state))

    ops = {
        'move':  op_move,
        'turn':  op_turn,
        'set':   op_set,
        'start': op_start,
        'stop':  op_stop,
    }

    def parse_value(token):
        """Литерал: число или строка."""
        try:
            return int(token)
        except ValueError:
            return token

    def run(program, state):
        stack = [state]
        for token in program.split():
            if token in ops:
                ops[token](stack)
            else:
                stack.append(parse_value(token))
        return stack.pop()

    return run