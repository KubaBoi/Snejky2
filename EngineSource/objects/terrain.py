from Engine.object import Object
from Engine.mesh import Mesh
from Engine.vertex import Vertex
from Engine.vector import Vector

class Terrain(Object):
    def __init__(self, position, scale=1, width=10, height=10):
        Object.__init__(self, position)

        self.scale = scale
        self.width = width
        self.height = height
        self.mesh = Mesh(self.Position)
        self.createVertices()

    def createVertices(self):
        self.mesh.verticesData = []
        self.mesh.triangles = []
        for x in range(self.width):
            for z in range(self.height):
                self.mesh.verticesData.append(Vertex(Vector(
                    self.Position.x + x,
                    self.Position.y,
                    self.Position.z + z
                )))

        i = 0
        for x in range(self.width-1):
            for z in range(self.height):
                if (i + self.width + 1 < len(self.mesh.verticesData)):
                    self.mesh.createTriangle(i + 1, i, i + self.width)
                    self.mesh.createTriangle(i + 1, i + self.width, i + self.width + 1)

                i += 1

        self.mesh.scale = self.scale

    def setHeights(self, heights):
        for v, h in zip(range(len(self.mesh.verticesData)), heights):
            vertex = self.mesh.verticesData[v]
            vertex.Position.y = h

            self.mesh.verticesData[v] = vertex


