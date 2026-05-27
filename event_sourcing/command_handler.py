from event_sourcing.events import Moved, Turned, ModeChanged, Started, Stopped
from event_sourcing.reducer import replay
import event_sourcing.pure_robot as pr


# CommandHandler — это мозг всей схемы.
# Когда приходит команда, я каждый раз делаю одно и то же:
# сначала читаю события робота и пересобираю из них текущее состояние,
# потом смотрю на команду и решаю, можно ли её выполнить с учётом этого
# состояния, и если да — превращаю её в события и дописываю их в стор.
class CommandHandler:
    def __init__(self, store):
        self.store = store

    def handle(self, robot_id, command):
        # пересобираю состояние из прошлых событий
        state = replay(self.store.load(robot_id))
        # решаю, какие события породит эта команда
        new_events = self._decide(state, command)
        # дописываю их в стор
        self.store.append(robot_id, new_events)
        return new_events

    def _decide(self, state, command):
        # Тут живут бизнес-правила: превращаю команду (намерение)
        # в события (факты). Команду могу и отклонить — тогда вернётся [].
        cmd = command[0]

        if cmd == 'move':
            return [Moved(command[1])]

        if cmd == 'turn':
            return [Turned(command[1])]

        if cmd == 'set':
            modes = {'water': pr.WATER, 'soap': pr.SOAP, 'brush': pr.BRUSH}
            if command[1] not in modes:
                return [] # незнакомый режим — отклоняю команду
            return [ModeChanged(command[1])]

        if cmd == 'start':
            return [Started()]

        if cmd == 'stop':
            return [Stopped()]

        return [] # незнакомая команда — ничего не пишу