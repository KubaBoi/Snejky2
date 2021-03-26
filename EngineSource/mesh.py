"""
vertices - seznam vertexu meshe 
triangles - index odkazujici na vertexy ve vertices (musi byt delitelny 3)
colors - barvy (razene podle triangles a vertices)
"""

import pygame

class Mesh:
    def __init__(self):
        self.vertices = None
        self.triangles = None
        self.colors = None

        self.defaultColor = (255,0,255)

    def updateMesh(self):
        pass

    def drawMesh(self, screen, camera):
        for v in self.vertices:
            v.update(camera)

        for t in range(len(self.triangles)):
            v1 = self.triangles[t]
            v2 = self.triangles[t + 1]
            v3 = self.triangles[t + 2]

            if (len(self.colors) > int(t/3)):
                color = self.colors[int(t/3)]
            else:
                color = self.defaultColor

            pygame.draw.polygon(screen, color,
                        [self.vertices[v1].projection,
                        self.vertices[v2].projection,
                        self.vertices[v3].projection], width=0)

            t += 2
            if (t >= len(self.triangles) - 1):
                break

    def setVertices(self, vertices):
        self.vertices = vertices

    def setTriangles(self, triangles):
        self.triangles = triangles

    def setColors(self, colors):
        self.colors = colors