from modular_cleaner import Cleaner, run, transfer_to_cleaner


def main() -> None:
    cleaner = Cleaner(transfer_to_cleaner)
    run(cleaner, (
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop',
    ))


if __name__ == '__main__':
    main()