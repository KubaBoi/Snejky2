from Engine.mesh import Mesh
from Engine.vector import Vector

class Object:
    def __init__(self, position, rotation=Vector(0,0,0)):
        self.Position = position
        self.Rotation = rotation
        self.mesh = None

    def update(self):
        if (self.mesh != None):
            self.mesh.Position = self.Position
            self.mesh.Rotation = self.Rotation
            self.mesh.updateMesh()

    def draw(self, gameScreen):
        if (self.mesh != None):
            self.mesh.drawMesh(gameScreen)

    def loadMesh(self, mesh, scale=1, color=(255,0,255)):
        self.mesh = Mesh(self.Position)
        self.mesh.loadMesh(mesh, scale, color)