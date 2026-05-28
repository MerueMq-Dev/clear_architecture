from stream_processing.events import RobotMoved, RobotTurned, ModeChanged, Started, Stopped


# главный процессор: заявка

def on_move(event, store):  store.publish(RobotMoved(event.distance))
def on_turn(event, store):  store.publish(RobotTurned(event.angle))
def on_mode(event, store):  store.publish(ModeChanged(event.mode))
def on_start(_, store): store.publish(Started())
def on_stop(_, store):  store.publish(Stopped())


# независимый процессор: печатает все эвенты

def log_result(event, _):
    print('  эвент:', event)