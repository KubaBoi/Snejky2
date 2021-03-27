from Engine.object import Object
from Engine.mesh import Mesh
from Engine.vector import Vector

class Penguin(Object):
    def __init__(self, position, scale, engine, color=(255,0,255)):
        Object.__init__(self, position)

        self.scale = scale

        self.body = Object(position)
        self.body.loadMesh("Engine/meshes/penguin/penguinBody.json", scale)

        self.head = Object(Vector(position.x,
                            position.y + 1,
                            position.z))
        self.head.loadMesh("Engine/meshes/penguin/penguinHead.json", scale)

        self.peak = Object(Vector(position.x,
                            position.y + 1.1,
                            position.z + 0.3))
        self.peak.loadMesh("Engine/meshes/penguin/penguinPeak.json", scale)

        self.legL = Object(Vector(position.x - 0.3,
                            position.y - 0.9,
                            position.z + 0.7))
        self.legL.loadMesh("Engine/meshes/penguin/penguinLeg.json", scale)

        self.legP = Object(Vector(position.x + 0.3,
                            position.y - 0.9,
                            position.z + 0.7))
        self.legP.loadMesh("Engine/meshes/penguin/penguinLeg.json", scale)

        self.handL = Object(Vector(position.x - 0.55,
                            position.y,
                            position.z))
        self.handL.loadMesh("Engine/meshes/penguin/penguinHand.json", scale)

        self.handP = Object(Vector(position.x + 0.55,
                            position.y,
                            position.z))
        self.handP.loadMesh("Engine/meshes/penguin/penguinHand.json", scale)

        engine.addObject(self.body)
        engine.addObject(self.head)
        engine.addObject(self.peak)
        engine.addObject(self.legL)
        engine.addObject(self.legP)
        engine.addObject(self.handL)
        engine.addObject(self.handP)

    def update(self):
        self.head.Position = Vector(self.Position.x,
                            self.Position.y + self.scale,
                            self.Position.z)

        self.peak.Position = Vector(self.Position.x,
                            self.Position.y + 1.1,
                            self.Position.z + 0.3)

        self.legL.Position = Vector(self.Position.x - 0.3,
                            self.Position.y - 0.9,
                            self.Position.z + 0.7)

        self.legP.Position = Vector(self.Position.x + 0.3,
                            self.Position.y - 0.9,
                            self.Position.z + 0.7)

        self.handL.Position = Vector(self.Position.x - 0.55,
                            self.Position.y,
                            self.Position.z)

        self.handP.Position = Vector(self.Position.x + 0.55,
                            self.Position.y,
                            self.Position.z)

        self.body.Position = self.Position