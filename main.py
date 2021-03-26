from Engine.engine import Engine
from Engine.vector import Vector

from Engine.object import Object
from Engine.objects.cube import Cube
from Engine.objects.pyramid import Pyramid
from Engine.objects.penguin import Penguin
import time

engine = Engine()

cube1 = Cube(Vector(-5, -5, 0), 1)
#engine.addObject(cube1)

pyramid = Pyramid(Vector(-5, 0, 0), 2, color=(200, 30, 30))
#engine.addObject(pyramid)

#loadedObject = Object(Vector(0, 0, -10))
#loadedObject.loadMesh("Engine/meshes/penguin.json")
#engine.addObject(loadedObject)

penguin = Penguin(Vector(0,0,-10), 1, engine)
engine.addObject(penguin)

run = True
while run:
    #t = time.time()
    cube1.Position.x += 0.005
    engine.update()

    #print("Time: " + str(time.time() - t))