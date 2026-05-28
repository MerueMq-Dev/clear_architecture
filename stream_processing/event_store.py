from collections import deque


class EventStore:
    def __init__(self):
        self._log = []          # вся история сообщений
        self._subs = {}         # тип сообщения список процессоров
        self._queue = deque()
        self._busy = False

    def subscribe(self, event_type, handler):
        self._subs.setdefault(event_type, []).append(handler)

    def publish(self, event):
        self._queue.append(event)
        if self._busy:
            return
        self._busy = True
        while self._queue:
            e = self._queue.popleft()
            self._log.append(e)
            for h in self._subs.get(type(e), []):
                h(e, self)
        self._busy = False

    def history(self):
        return list(self._log)