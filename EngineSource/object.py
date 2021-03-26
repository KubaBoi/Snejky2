from Engine.mesh import Mesh

class Object:
    def __init__(self, position):
        self.Position = position
        self.mesh = None
        self.defaultColor = (255,0,255)

    def update(self):
        if (self.mesh != None):
            self.mesh.Position = self.Position
            self.mesh.updateMesh()

    def draw(self, gameScreen):
        if (self.mesh != None):
            self.mesh.drawMesh(gameScreen)

    def loadMesh(self, mesh, scale=1, color=(255,0,255)):
        self.mesh = Mesh(self.Position)
        self.mesh.loadMesh(mesh, scale, color)