from Engine.object import Object
from Engine.mesh import Mesh

class Pyramid(Object):
    def __init__(self, position, scale, color=(255,0,255)):
        Object.__init__(self, position)

        self.loadMesh("Engine/meshes/pyramid.json", scale, color)