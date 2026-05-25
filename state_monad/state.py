class State:
    def __init__(self, run):
        self.run = run

    def bind(self, f):
        # Выполнить себя, отдать результат функции f, выполнить то, что она вернёт.
        def new_run(state):
            result, state2 = self.run(state)
            return f(result).run(state2)
        return State(new_run)

    def __rshift__(self, other):
        # Оператор >> : выполнить левое, прокинуть состояние в правое
        # (результат левого здесь не нужен, поэтому _).
        return self.bind(lambda _: other)

    @staticmethod
    def unit(value):
        # Завернуть готовое значение в монаду, не меняя состояние.
        return State(lambda state: (value, state))