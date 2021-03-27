"""
uchovává, vykresluje a spravuje objekty
obsuhuje i pygame scene
"""

import pygame
from Engine.camera import Camera
from Engine.vector import Vector
from Engine.light import Light

class GameScreen:
    def __init__(self, width=1280, height=720, color=(255, 255, 255), fullScreen=False):
        self.width = width
        self.height = height

        #full screen
        if (fullScreen):
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))

        self.color = color
        self.screen.fill((self.color))

        self.Objects = []
        self.Lights = []
        self.camera = Camera(Vector(0,0,0), width/2, height/2)
        self.Lights.append(Light(Vector(0,0,0)))

        #seznam prave se vykreslujicich trojuhelniku 
        #face je (vertex, vertex, vertex)
        self.faces = []

    def update(self):
        self.camera.update()
        for o in self.Objects:
            o.update()
        
        self.bubbleSort()

    def draw(self):
        self.screen.fill((self.color))

        for o in self.Objects:
            o.draw(self)

        #for f in self.faces:


        self.drawCursor()

        pygame.display.flip()

    def addObject(self, obj):
        self.Objects.append(obj)

    def removeObject(self, obj):
        self.Objects.remove(obj)

    def bubbleSort(self):
        for i in range(len(self.Objects) - 1):
            for j in range(len(self.Objects) - i - 1):
                if (self.Objects[j].Position.distance(self.camera.Position) < 
                    self.Objects[j + 1].Position.distance(self.camera.Position)):
                    tmp = self.Objects[j]
                    self.Objects[j] = self.Objects[j + 1]
                    self.Objects[j + 1] = tmp

    def drawCursor(self):
        pygame.draw.line(self.screen, (0,0,0),
                         (self.width/2-5, self.height/2),
                         (self.width/2+5, self.height/2))
        pygame.draw.line(self.screen, (0,0,0),
                         (self.width/2, self.height/2-5),
                         (self.width/2, self.height/2+5))