import concat_interpreter.pure_robot as pr
from concat_interpreter.transfers import console_transfer
from concat_interpreter.interpreter import make_interpreter


# Клиентская сторона
WORKFLOW = "100 move -90 turn soap set start 50 move stop"

if __name__ == "__main__":
    run = make_interpreter(console_transfer)
    initial = pr.RobotState(0.0, 0.0, 0.0, 0)

    final = run(WORKFLOW, initial)
    print(final)