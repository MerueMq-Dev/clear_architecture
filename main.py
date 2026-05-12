import functional_di_robot.pure_robot as pr
from functional_di_robot.transfers import console_transfer
from functional_di_robot.injection import inject
from functional_di_robot.сlients  import run, navigator_commands, full_commands


SQUARE_ROUTE = [
    ('move', 10), ('turn', 90),
    ('move', 10), ('turn', 90),
    ('move', 10), ('turn', 90),
    ('move', 10), ('turn', 90),
]

SHORT_ROUTE = [
    ('move', 5), ('turn', 45), ('move', 3),
]

CLEAN_PLAN = [
    ('set', 'soap'), ('start', None),
    ('move', 10), ('turn', 90), ('move', 10),
    ('stop', None),
]


if __name__ == "__main__":
    # Точка сборки
    api = inject(console_transfer)
    state = pr.RobotState(0.0, 0.0, 0.0, 0)

    navigator = navigator_commands(api)
    full      = full_commands(api)

    print("--- квадрат ---")
    state = run(navigator, SQUARE_ROUTE, state)

    print("--- короткий маршрут ---")
    state = run(navigator, SHORT_ROUTE, state)

    print("--- патруль с уборкой ---")
    state = run(full, CLEAN_PLAN, state)