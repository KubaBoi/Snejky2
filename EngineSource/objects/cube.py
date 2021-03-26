from Engine.object import Object
from Engine.mesh import Mesh
from Engine.vertex import Vertex
from Engine.vector import Vector

class Cube(Object):
    def __init__(self, position):
        Object.__init__(self, position)

        self.mesh = Mesh()