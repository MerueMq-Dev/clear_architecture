from either.responses import OK, is_ok


class StateMonad:
    def __init__(self, state, log=None, response=OK):
        self.state = state
        self.log = log or []
        self.response = response

    def bind(self, func):
        # КЛЮЧЕВОЕ МЕСТО жёсткой версии:
        # если уже была ошибка — следующий шаг просто пропускается.
        if not is_ok(self.response):
            return self

        new_state, new_log, new_response = func(self.state, self.log)
        return StateMonad(new_state, new_log, new_response)

    def ok(self):
        return is_ok(self.response)