from cleaner.cleaner import Cleaner, CleaningMode


def transfer(message):
    print(message)


if __name__ == "__main__":
    initial = Cleaner(transfer)

    final = (initial
             .move(100)
             .turn(-90)
             .set_mode(CleaningMode.SOAP)
             .start()
             .move(50)
             .stop())

    print("\n--- финальное состояние ---")
    print(final)

    print("\n--- initial остался прежним ---")
    print(initial)

    print("\n--- проверка иммутабельности ---")
    try:
        initial.x = 999
    except Exception as e:
        print(f"{type(e).__name__}: {e}")