"""
Event Store — единственное место, которое я разрешаю себе менять.
Всё остальное в системе чистое и состояния не держит.

Храню события отдельно по каждому роботу. Делать со стором можно
по сути только две вещи: дописать события в конец и прочитать их.
Удалять или править события нельзя — только добавлять новые.
"""

class EventStore:
    def __init__(self):
        self._streams = {}   # robot_id -> список его событий

    def append(self, robot_id, events):
        # Дописываю новые события в хвост — старые не трогаю.
        self._streams.setdefault(robot_id, []).extend(events)

    def load(self, robot_id):
        # Читаю все события робота.
        return list(self._streams.get(robot_id, []))

    def count(self, robot_id):
        return len(self._streams.get(robot_id, []))