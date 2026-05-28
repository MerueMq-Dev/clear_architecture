from stream_processing.events import (
    MoveRequested, TurnRequested, ModeRequested,
    StartRequested, StopRequested,
)


def make_request(command):
    cmd = command[0]
    if cmd == 'move':  return MoveRequested(command[1])
    if cmd == 'turn':  return TurnRequested(command[1])
    if cmd == 'set':   return ModeRequested(command[1])
    if cmd == 'start': return StartRequested()
    if cmd == 'stop':  return StopRequested()
    return None


def handle_command(store, command):
    request = make_request(command)
    if request is not None:
        store.publish(request)