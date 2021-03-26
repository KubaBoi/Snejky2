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

    def drawMesh(self, screen, camera):
        for v in self.vertices:
            

        pygame.draw.polygon(screen, (0,255,0), [(152, 190), (152, 230), (1056, 230),(1056, 190)],True)

    def setVertices(self, vertices):
        self.vertices = vertices

    def setTriangles(self, triangles):
        self.triangles = triangles

    def setColors(self, colors):
        self.colors = colors