
# Универсальный исполнитель
def run(dispatch, program, state):
    for command in program:
        state = dispatch(command, state)
    return state

# Навигатор. Получает ОДНУ функцию-зависимость
def navigate(dispatch, route, state):
    for step in route:
        state = dispatch(step, state)
    return state