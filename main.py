from di_robot.robot import Robot, ConsoleLogger
from di_robot.robot_api import RobotAPI


def main() -> None:
    transfer = ConsoleLogger()
    robot = Robot(logger=transfer)
    api = RobotAPI(robot=robot)

    api.set_mode("soap")
    api.start()
    api.move(100)
    api.turn(90)
    api.stop()

if __name__ == '__main__':
    main()