"""
Клиент: собирает СПИСОК команд (ничего не выполняя),
затем отдаёт его исполнителю — все команды выполняются разом.
"""
import  command.pure_robot as pr
from command.commands import Move, Turn, SetState, Start, Stop
from command.executor import run_batch


def transfer_to_cleaner(message):
    print(message)


# Клиент только СОЗДАЁТ команды — робот пока не двигается.
batch = [
    Move(100),
    Turn(-90),
    SetState('soap'),
    Start(),
    Move(50),
    Stop(),
]


if __name__ == "__main__":
    initial = pr.RobotState(0.0, 0.0, 0.0, pr.WATER)

    final = run_batch(transfer_to_cleaner, batch, initial)

    print("--- финальное состояние ---")
    print(final)