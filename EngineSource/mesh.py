"""
vertices - seznam vertexu meshe 
triangles - index odkazujici na vertexy ve vertices (musi byt delitelny 3)
colors - barvy (razene podle triangles a vertices)
"""

import pygame
import math
import json

from Engine.vector import Vector
from Engine.vertex import Vertex

class Mesh:
    def __init__(self, position):
        self.Position = position
        self.vertices = None
        self.triangles = None
        self.colors = None

        self.defaultColor = (255,0,255)

    def updateMesh(self):
        self.vertices = []
        for v in self.meshData["vertices"]:
            self.vertices.append(Vertex(Vector(self.Position.x + v[0]*self.scale,
                                        self.Position.y + v[1]*self.scale,
                                        self.Position.z + v[2]*self.scale)))

    def drawMesh(self, gameScreen):
        for v in self.vertices:
            v.update(gameScreen.camera)

        for t in range(0, len(self.triangles), 3):
            v1 = self.triangles[t]
            v2 = self.triangles[t + 1]
            v3 = self.triangles[t + 2]

            n = self.calculateNormal(self.vertices[v1], self.vertices[v2], self.vertices[v3])
            cP = self.vertices[v1].Position.newVector(gameScreen.camera.Position)
            #face je "zady" ke kamere
            if (n.angle(cP) > math.pi/2):
                continue

            if (len(self.colors) > int(t/3)):
                color = self.colors[int(t/3)]
            else:
                color = self.defaultColor

            color = self.calculateColor(n, self.vertices[v1], color, gameScreen.Lights)

            pygame.draw.polygon(gameScreen.screen, color,
                        [self.vertices[v1].projection,
                        self.vertices[v2].projection,
                        self.vertices[v3].projection], width=0)

            pygame.draw.polygon(gameScreen.screen, (0,0,0),
                        [self.vertices[v1].projection,
                        self.vertices[v2].projection,
                        self.vertices[v3].projection], width=1)

    def calculateColor(self, n, v1, color, lights):
        brightness = 1/2
        for l in lights:
            lv = v1.Position.newVector(l.Position)
            multiplier = 2 #mozno pouzit jako nastaveni jasu
            angle = int((lv.angle(n)*180 / math.pi)*brightness)

        color = (color[0] - angle,
                color[1] - angle,
                color[2] - angle)

        return self.repairColor(color)

    def calculateNormal(self, v1, v2, v3):
        v = v1.Position.newVector(v2.Position)
        u = v1.Position.newVector(v3.Position)

        #normalovy vektor k rovine face
        return Vector(u.y*v.z - v.y*u.z,
                    u.z*v.x - v.z*u.x,
                    u.x*v.y - v.x*u.y)

    def repairColor(self, color):
        r = color[0]
        g = color[1]
        b = color[2]

        if (r < 0): r = 0
        elif (r > 255): r = 255

        if (g < 0): g = 0
        elif (g > 255): g = 255

        if (b < 0): b = 0
        elif (b > 255): b = 255

        return (int(r), int(g), int(b))

    def setVertices(self, vertices):
        self.vertices = vertices

    def setTriangles(self, triangles):
        self.triangles = triangles

    def setColors(self, colors):
        self.colors = colors

    def loadMesh(self, mesh, scale, color):
        self.scale = scale

        x = self.Position.x
        y = self.Position.y
        z = self.Position.z

        with open(mesh, "r") as m:
            self.meshData = json.load(m)

        self.vertices = []
        for v in self.meshData["vertices"]:
            self.vertices.append(Vertex(Vector(x + v[0]*self.scale,
                                        y + v[1]*self.scale,
                                        z + v[2]*self.scale)))

        self.triangles = []
        for t in self.meshData["triangles"]:
            self.createTriangle(t[0], t[1], t[2])

        #v json jsou data o barve
        if ("colors" in self.meshData):
            self.colors = []
            for c in self.meshData["colors"]:
                self.colors.append(c)
        else:
            self.createColor(color)

    def createTriangle(self, i1, i2, i3):
        self.triangles.append(i1)
        self.triangles.append(i2)
        self.triangles.append(i3)

    def createColor(self, color):
        self.colors = []
        for i in range(int(len(self.triangles)/3)):
            self.colors.append(color)