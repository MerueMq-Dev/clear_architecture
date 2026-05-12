"""
Клиенты — универсальный исполнитель и фабрики таблиц команд.

Каждая фабрика описывает интерфейс конкретного клиента: какие
имена шагов он понимает и какие функции за ними стоят. Это
функциональный аналог "узкого интерфейса" из ISP.
"""

# Универсальный исполнитель программы
def run(commands, program, state):
    for action, value in program:
        state = commands[action](value, state)
    return state


# Интерфейс навигатора: только перемещение
def navigator_commands(api):
    return {
        'move': api['move'],
        'turn': api['turn'],
    }

# Полный интерфейс: перемещение + управление чисткой.
def full_commands(api):
    return {
        'move':  api['move'],
        'turn':  api['turn'],
        'set':   api['set_state'],
        'start': lambda _, state: api['start'](state),
        'stop':  lambda _, state: api['stop'](state),
    }