from functools import reduce
import pure_robot as pr
from events import Moved, Turned, ModeChanged, Started, Stopped

# Здесь я собираю состояние робота из событий.

# Заглушка вместо transfer: при пересчёте состояния вывод мне не нужен.
_silent = lambda message: None

def initial_state():
    return pr.RobotState(0.0, 0.0, 0.0, pr.WATER)

# apply — это мой "обработчик одного события": беру текущее состояние
# и событие, возвращаю новое состояние. Никаких побочных эффектов:
# когда я восстанавливаю состояние, я ничего не шлю реальному роботу,
# а просто пересчитываю, где он оказался бы.
def apply(state, event):
    # Просто смотрю, что за событие, и применяю нужную функцию робота.
    if isinstance(event, Moved):
        return pr.move(_silent, event.dist, state)
    if isinstance(event, Turned):
        return pr.turn(_silent, event.angle, state)
    if isinstance(event, ModeChanged):
        return pr.set_state(_silent, event.mode, state)
    if isinstance(event, Started):
        return pr.start(_silent, state)
    if isinstance(event, Stopped):
        return pr.stop(_silent, state)
    return state


# replay прогоняет все события через apply (обычный fold) и даёт
# текущее состояние.
def replay(events):
    # Собираю состояние с чистого листа, проиграв все события.
    return reduce(apply, events, initial_state())