from Engine.engine import Engine
from Engine.vector import Vector

from Engine.object import Object
from Engine.objects.cube import Cube
import time

engine = Engine()

cube1 = Cube(Vector(-5, -5, 0), 1)
engine.addObject(cube1)
loadedCube = Object(Vector(-5, 5, 0))
loadedCube.loadMesh("Engine/meshes/cube.json")
engine.addObject(loadedCube)

run = True
while run:
    #t = time.time()
    cube1.Position.x += 0.005
    loadedCube.Position.x += 0.005
    engine.update()

    #print("Time: " + str(time.time() - t))