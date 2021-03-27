import math

from Engine.vector import Vector

class Light:
    def __init__(self, position):
        self.Position = position
        self.angle = 0

    def Update(self):
        #self.angle += 0.01
        self.Position.x = math.sin(self.angle)
        self.Position.z = math.cos(self.angle)