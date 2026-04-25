from . import states
from .cleaner import Cleaner

def execute(cleaner: Cleaner, command: str) -> None:
    match command.split():
        case ['move', distance]:
            cleaner.move(int(distance))
        case ['turn', angle]:
            cleaner.turn(int(angle))
        case ['set', mode]:
            cleaner.set_state(states.parse(mode))
        case ['start']:
            cleaner.start()
        case ['stop']:
            cleaner.stop()
        case _:
            cleaner.transfer(f'UNKNOWN {command}')

def run(cleaner, code):
    for command in code:
        execute(cleaner, command)