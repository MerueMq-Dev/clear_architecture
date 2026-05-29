from  ast_interpreter.ast_nodes import Move, Turn, SetState, Start, Stop
from ast_interpreter.interpreter import RealInterpreter, SOAP as SOAP_MODE
from ast_interpreter.analyzer import analyze


# сценарий 1: прямая программа, без реакции на ответы
simple_program = Move(50, lambda _:
    Turn(90, lambda _:
        SetState(SOAP_MODE, lambda _:
            Start(lambda _:
                Move(30, lambda _:
                    Stop())))))


# Сценарий 2: программа реагирует на ответ
# Если первый move упёрся в стену — поворачиваем и пробуем в другую сторону.
# Если прошёл нормально — продолжаем по плану.

def smart_program():
    def after_first_move(response):
        if response.ok:
            # всё нормально, идём дальше
            return SetState(SOAP_MODE, lambda _: Stop())
        else:
            # упёрлись в стену -> разворот и попытка №2
            return Turn(180, lambda _:
                Move(20, lambda _:
                    SetState(SOAP_MODE, lambda _:
                        Stop())))

    return Move(200, after_first_move)   # 200 точно выйдет за границу


if __name__ == "__main__":
    # анализ дерева
    print("--- анализ простой программы ---")
    print(dict(analyze(simple_program)))

    # реальное выполнение простой программы
    print("\n--- выполнение простой программы ---")
    interp = RealInterpreter()
    interp.run(simple_program)
    print("состояние:", interp.state)
    print("лог:")
    for line in interp.log:
        print(" ", line)

    # выполнение умной программы с реакцией на barrier
    print("\n--- выполнение умной программы (упрётся в стену) ---")
    interp2 = RealInterpreter()
    interp2.run(smart_program())
    print("состояние:", interp2.state)
    print("лог:")
    for line in interp2.log:
        print(" ", line)