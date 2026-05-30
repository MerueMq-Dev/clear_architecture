from capabilities.api import create_robot
from capabilities.robot import Mode


    # Создаём transfer, который помечает сообщения именем сценария.
def make_transfer(scenario_name):
    def transfer(msg):
        print(f"  [{scenario_name}] {msg}")
    return transfer


    # Показываем текущий тип набора и доступные операции
def show_caps(caps):
    name = type(caps).__name__
    ops = [m for m in dir(caps)
           if not m.startswith('_') and m not in ('info',)]
    print(f"  -> сейчас: {name}, доступно: {ops}")


    # Базовый сценарий: всё проходит по плану.
def scenario_happy_path():
    print("=" * 60)
    print("СЦЕНАРИЙ 1: счастливый путь")
    print("=" * 60)
    caps = create_robot(make_transfer("happy"))

    caps = caps.move(50)
    caps = caps.soap()
    caps = caps.start()
    caps = caps.stop()
    show_caps(caps)
    print(f"  итог: {caps.info()}")



    # Робот упирается в стену, потом отворачивается и продолжает
def scenario_wall_recovery():
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: стена и восстановление")
    print("=" * 60)
    caps = create_robot(make_transfer("wall"))

    caps = caps.move(200)             # упрётся в стену
    show_caps(caps)                   # -> Stuck

    # У Stuck нет .move — проверим
    has_move = hasattr(caps, 'move')
    print(f"  hasattr(caps, 'move'): {has_move}")

    caps = caps.turn(180)             # отвернулись
    show_caps(caps)                   # -> Idle снова

    caps = caps.move(30)              # теперь можно ехать
    print(f"  итог: {caps.info()}")


    # Мыло заканчивается, и .soap пропадает как атрибут.
def scenario_resource_depletion():
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: исчерпание ресурса")
    print("=" * 60)
    caps = create_robot(make_transfer("resource"),
                        resources={Mode.WATER: 999, Mode.SOAP: 1, Mode.BRUSH: 999})

    # первая чистка мылом
    caps = caps.soap()
    caps = caps.start()
    caps = caps.stop()
    print(f"  после первой чистки ресурсы: {caps.info()['resources']}")

    # пробуем выставить soap снова — атрибута уже нет
    has_soap = hasattr(caps, 'soap')
    print(f"  hasattr(caps, 'soap'): {has_soap}")

    try:
        caps.soap
    except AttributeError as e:
        print(f"  caps.soap -> AttributeError (как и ожидалось)")

    # но другие режимы доступны
    caps = caps.water()
    print(f"  переключились на water, итог: {caps.info()}")


    # Во время чистки нельзя двигаться и менять режим
def scenario_cleaning_mode_restrictions():
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 4: ограничения во время чистки")
    print("=" * 60)
    caps = create_robot(make_transfer("cleaning"))

    caps = caps.start()
    show_caps(caps)                          # -> Cleaning

    print(f"  hasattr(caps, 'move'):  {hasattr(caps, 'move')}")
    print(f"  hasattr(caps, 'soap'):  {hasattr(caps, 'soap')}")
    print(f"  hasattr(caps, 'turn'):  {hasattr(caps, 'turn')}")
    print(f"  hasattr(caps, 'stop'):  {hasattr(caps, 'stop')}")

    # повернуться во время чистки можно
    caps = caps.turn(45)
    caps = caps.stop()
    show_caps(caps)                          # -> Idle
    print(f"  итог: {caps.info()}")


    # Старые caps остаются валидны — иммутабельность.
def scenario_history_preserved():
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 5: иммутабельность истории")
    print("=" * 60)
    initial = create_robot(make_transfer("history"))

    after_move = initial.move(40)
    after_turn = after_move.turn(90)

    print(f"  initial   : {initial.info()['position']}")
    print(f"  after_move: {after_move.info()['position']}")
    print(f"  after_turn: {after_turn.info()['position']}, angle={after_turn.info()['angle']}")

    # initial всё ещё валиден — у него своя ветка
    branch = initial.move(70)
    print(f"  branch (другая ветка из initial): {branch.info()['position']}")


if __name__ == "__main__":
    scenario_happy_path()
    scenario_wall_recovery()
    scenario_resource_depletion()
    scenario_cleaning_mode_restrictions()
    scenario_history_preserved()