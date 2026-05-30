from capabilities.api import create_robot


def transfer(msg):
    print(msg)


robot = create_robot(transfer)

print(type(robot).__name__)
# Idle


robot = robot.move(50)

robot = robot.start()

print(type(robot).__name__)
# Cleaning