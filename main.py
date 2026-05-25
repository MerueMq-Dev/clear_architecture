import state_monad.pure_robot as pr
from state_monad.robot_operations import move, turn, set_state, start, stop

# Цепочка строится оператором >> и читается как конвейер.
# Ничего не выполняется, пока не вызван .run(начальное_состояние).
workflow = (
    move(100)
    >> turn(-90)
    >> set_state('soap')
    >> start()
    >> move(50)
    >> stop()
)


if __name__ == "__main__":
    initial_robot = pr.RobotState(0.0, 0.0, 0.0, pr.WATER)
    initial_state = (initial_robot, [])   # (робот, пустой лог)

    result, (final_robot, log) = workflow.run(initial_state)

    print("--- фоновый лог вычислений ---")
    for entry in log:
        print(entry)

    print("\n--- финальное состояние робота ---")
    print(final_robot)