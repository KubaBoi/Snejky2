from Engine.object import Object
from Engine.mesh import Mesh
from Engine.vertex import Vertex
from Engine.vector import Vector

class Cube(Object):
    def __init__(self, position, scale, color=(255,0,255)):
        Object.__init__(self, position)

        self.loadMesh("Engine/meshes/cube.json", scale, color)
