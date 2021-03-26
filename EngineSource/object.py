class Object:
    def __init__(self, position):
        self.position = position
        self.mesh = None

    def update(self):
        if (self.mesh != None):
            self.mesh.update()

    def draw(self, screen, camera):
        if (self.mesh != None):
            self.mesh.drawMesh(screen, camera)