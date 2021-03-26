from Engine.engine import Engine
from Engine.vector import Vector

from Engine.objects.cube import Cube

engine = Engine()

engine.addObject(Cube(Vector(0, 0, 0)))

run = True
while run:
    engine.update()