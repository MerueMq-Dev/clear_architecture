from collections import namedtuple

# События — это факты о том, что уже случилось. Они неизменяемы:
# случившееся не переписать. Главная идея Event Sourcing в том, что
# храню я именно события, а текущее состояние робота всегда могу
# пересчитать, прогнав их заново.

# Беру namedtuple — мне нужны просто неизменяемые "факты" с парой полей.
Moved = namedtuple("Moved", "dist") # робот проехал столько-то
Turned = namedtuple("Turned", "angle") # повернул на угол
ModeChanged  = namedtuple("ModeChanged", "mode") # сменил режим
Started = namedtuple("Started", "") # начал чистку
Stopped = namedtuple("Stopped", "") # закончил чистку