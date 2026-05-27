from event_sourcing.event_store import EventStore
from event_sourcing.command_handler import CommandHandler
from event_sourcing.reducer import replay

ROBOT = "cleaner-1"



if __name__ == "__main__":
    store = EventStore()
    handler = CommandHandler(store)

    # Отправляю команды по одной.
    commands = [
        ('move', 100),
        ('turn', -90),
        ('set', 'soap'),
        ('start',),
        ('move', 50),
        ('stop',),
    ]
    for command in commands:
        handler.handle(ROBOT, command)

    # Смотрю, какие факты накопились в сторе.
    print("--- что накопилось в Event Store ---")
    for e in store.load(ROBOT):
        print(e)

    # Текущее состояние = проигрывание всех событий с нуля.
    print("\n--- текущее состояние (проиграл все события) ---")
    print(replay(store.load(ROBOT)))