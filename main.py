from either.robot_state import RobotState, WATER, SOAP
from either.state_monad import StateMonad
from either.operations import move, turn, set_state, start, stop


def show(title, result):
    print(f"--- {title} ---")
    print("финальное состояние:", result.state)
    print("итоговый ответ:     ", result.response)
    print("ok:                 ", result.ok())
    print("лог:")
    for line in result.log:
        print(" ", line)
    print()


if __name__ == "__main__":
    initial = lambda: StateMonad(RobotState(0.0, 0.0, 0.0, WATER))

    # 1. Всё хорошо: вода и мыло на месте, в границы укладываемся
    resources_ok = {'water': 1, 'soap': 1}
    happy = (initial()
        .bind(move(100))
        .bind(turn(-90))
        .bind(set_state(SOAP, resources_ok))
        .bind(start)
        .bind(move(50))                          # сейчас тоже упрётся в y < 0
        .bind(stop))
    show("ХОРОШИЙ путь", happy)

    # 2. Чтобы happy реально прошёл — отвернёмся внутрь поля,
    #    а сценарий с обрывом сделаем отдельно.
    really_happy = (initial()
        .bind(move(50))
        .bind(turn(90))                          # поворот ВВЕРХ, не вниз
        .bind(set_state(SOAP, resources_ok))
        .bind(start)
        .bind(move(50))                          # уедем в (50, 50)
        .bind(stop))
    show("ХОРОШИЙ путь без барьера", really_happy)

    # 3. Барьер в середине: всё после move(50) вниз — пропускается
    crash = (initial()
        .bind(move(100))
        .bind(turn(-90))
        .bind(set_state(SOAP, resources_ok))
        .bind(start)
        .bind(move(50))                          # BARRIER
        .bind(set_state(WATER, resources_ok))    # пропустится
        .bind(stop))                             # пропустится
    show("ОБРЫВ по барьеру", crash)

    # 4. Нет воды: ошибка раньше, дальнейшие шаги тоже не запускаются
    resources_dry = {'water': 0, 'soap': 1}
    dry = (initial()
        .bind(move(10))
        .bind(set_state(WATER, resources_dry))   # OUT_OF_WATER, цепочка стоп
        .bind(start)                             # пропустится
        .bind(move(20))                          # пропустится
        .bind(stop))                             # пропустится
    show("ОБРЫВ по ресурсам", dry)