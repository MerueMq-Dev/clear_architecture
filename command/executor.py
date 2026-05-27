from functools import reduce


# Исполнитель пакета команд.
def run_batch(transfer, commands, initial_state):
    return reduce(
        lambda state, command: command.execute(transfer, state),
        commands,
        initial_state,
    )