import functional_di_robot_2.pure_robot as pr
from  functional_di_robot_2.transfers import console_transfer
from  functional_di_robot_2.dispatch import make_dispatch
from  functional_di_robot_2.clients import run, navigate


SQUARE_ROUTE = [
    ('move', 10), ('turn', 90),
    ('move', 10), ('turn', 90),
    ('move', 10), ('turn', 90),
    ('move', 10), ('turn', 90),
]

CLEAN_PLAN = [
    ('set', 'soap'),
    ('start',),
    ('move', 10), ('turn', 90), ('move', 10),
    ('stop',),
]


if __name__ == "__main__":
    dispatch = make_dispatch(console_transfer)
    state = pr.RobotState(0.0, 0.0, 0.0, 0)

    print("--- квадрат ---")
    state = navigate(dispatch, SQUARE_ROUTE, state)

    print("--- патруль с уборкой ---")
    state = run(dispatch, CLEAN_PLAN, state)