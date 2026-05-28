from  stream_processing.robot_state import RobotState, CleaningMode
from stream_processing.event_store import EventStore
from stream_processing.command_handler import handle_command
from stream_processing.projector import project
from stream_processing.events import (
    MoveRequested, TurnRequested, ModeRequested, StartRequested, StopRequested,
    RobotMoved, RobotTurned, ModeChanged, Started, Stopped,
)
from stream_processing.processors import (
    on_move, on_turn, on_mode,
    on_start, on_stop, log_result
)


def setup(store):
    # главный процессор робота
    store.subscribe(MoveRequested,  on_move)
    store.subscribe(TurnRequested,  on_turn)
    store.subscribe(ModeRequested,  on_mode)
    store.subscribe(StartRequested, on_start)
    store.subscribe(StopRequested,  on_stop)

    for t in (RobotMoved, RobotTurned, ModeChanged, Started, Stopped):
        store.subscribe(t, log_result)


def main():
    store = EventStore()
    setup(store)

    commands = [
        ('move', 100),
        ('turn', -90),
        ('set', CleaningMode.SOAP),
        ('start',),
        ('move', 50),
        ('stop',),
    ]
    for c in commands:
        handle_command(store, c)

    initial = RobotState(0.0, 0.0, 0.0, CleaningMode.WATER.value)
    print('\n--- итоговое состояние ')
    print(project(store.history(), initial))

    print('\n--- история сообщений ')
    for i, e in enumerate(store.history(), 1):
        print(f'{i}: {e}')


if __name__ == '__main__':
    main()