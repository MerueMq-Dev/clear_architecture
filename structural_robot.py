import math

# --- Константы режимов очистки ---
WATER = "water"
SOAP = "soap"
BRUSH = "brush"


def create_robot():
    return {
        "x": 0.0,
        "y": 0.0,
        "angle": 0,
        "cleaning_type": WATER,
        "is_working": False,
    }


def move(robot, distance):
    rad = math.radians(robot["angle"])
    robot["x"] += distance * math.cos(rad)
    robot["y"] += distance * math.sin(rad)
    print(f"POS {robot['x']},{robot['y']}")


def turn(robot, degrees):
    robot["angle"] += degrees
    print(f"ANGLE {robot['angle']}")


def set(robot, cleaning_type):
    robot["cleaning_type"] = cleaning_type
    print(f"STATE {cleaning_type}")


def start(robot):
    robot["is_working"] = True
    print(f"START WITH {robot['cleaning_type']}")


def stop(robot):
    robot["is_working"] = False
    print("STOP")


def execute_command(robot, command):
    parts = command.strip().split()
    name = parts[0]

    if name == "move":
        move(robot, int(parts[1]))
    elif name == "turn":
        turn(robot, int(parts[1]))
    elif name == "set":
        set(robot, parts[1])
    elif name == "start":
        start(robot)
    elif name == "stop":
        stop(robot)
    else:
        print(f"Unknown command: {name}")


def run_program(commands):
    robot = create_robot()
    for command in commands:
        execute_command(robot, command)


def start_example():
    code = (
        "move 100",
        "turn -90",
        "set soap",
        "start",
        "move 50",
        "stop",
    )
    run_program(code)