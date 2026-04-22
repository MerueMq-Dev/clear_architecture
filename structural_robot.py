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


def move_robot(robot, distance):
    rad = math.radians(robot["angle"])
    robot["x"] += distance * math.cos(rad)
    robot["y"] += distance * math.sin(rad)
    print(f"POS {robot['x']},{robot['y']}")


def turn_robot(robot, degrees):
    robot["angle"] += degrees
    print(f"ANGLE {robot['angle']}")


def set_cleaning_type(robot, cleaning_type):
    robot["cleaning_type"] = cleaning_type
    print(f"STATE {cleaning_type}")


def start_cleaning(robot):
    robot["is_working"] = True
    print(f"START WITH {robot['cleaning_type']}")


def stop_cleaning(robot):
    robot["is_working"] = False
    print("STOP")


def execute_command(robot, command):
    parts = command.strip().split()
    name = parts[0]

    if name == "move":
        move_robot(robot, int(parts[1]))
    elif name == "turn":
        turn_robot(robot, int(parts[1]))
    elif name == "set":
        set_cleaning_type(robot, parts[1])
    elif name == "start":
        start_cleaning(robot)
    elif name == "stop":
        stop_cleaning(robot)
    else:
        print(f"Unknown command: {name}")


def run_program(commands):
    robot = create_robot()
    for command in commands:
        execute_command(robot, command)


def start():
    code = (
        "move 100",
        "turn -90",
        "set soap",
        "start",
        "move 50",
        "stop",
    )
    run_program(code)