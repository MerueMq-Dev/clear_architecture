from collections import namedtuple


RobotState = namedtuple("RobotState", "x y angle state")

WATER = 1
SOAP  = 2
BRUSH = 3