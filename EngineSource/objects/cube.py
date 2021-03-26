from Engine.object import Object
from Engine.mesh import Mesh
from Engine.vertex import Vertex
from Engine.vector import Vector

class Cube(Object):
    def __init__(self, position):
        Object.__init__(self, position)

        self.mesh = Mesh()

        vertices = []
        vertices.append(Vertex(Vector(1,10,10)))
        vertices.append(Vertex(Vector(1,0,10)))
        vertices.append(Vertex(Vector(10,10,10)))

        triangles = []
        triangles.append(0)
        triangles.append(1)
        triangles.append(2)

        colors = []
        colors.append((30, 20, 255))

        self.mesh.setVertices(vertices)
        self.mesh.setTriangles(triangles)
        self.mesh.setColors(colors)
