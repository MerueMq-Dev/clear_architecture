from public_api import pure_robot as robot

def initial_state():
    return robot.RobotState(x=0, y=0, angle=0, state=robot.WATER)

def move(distance: int, state: robot.RobotState) -> robot.RobotState:
    return robot.move(robot.transfer_to_cleaner, distance, state)

def turn(angle: int, state: robot.RobotState) -> robot.RobotState:
    return robot.turn(robot.transfer_to_cleaner, angle, state)

def set_mode(mode: str, state: robot.RobotState) -> robot.RobotState:
    return robot.set_state(robot.transfer_to_cleaner, mode, state)

def start(state: robot.RobotState) -> robot.RobotState:
    return robot.start(robot.transfer_to_cleaner, state)

def stop(state: robot.RobotState) -> robot.RobotState:
    return robot.stop(robot.transfer_to_cleaner, state)

def run_script(commands: list[str], state: robot.RobotState) -> robot.RobotState:
    return robot.make(robot.transfer_to_cleaner, commands, state)