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
        self.camera = Camera(Vector(0,0,-20), width/2, height/2)
        self.Lights.append(Light(Vector(0,0,-20)))

    def update(self):
        self.camera.update()
        for o in self.Objects:
            o.update()

    def draw(self):
        self.screen.fill((self.color))
        pygame.draw.line(self.screen, (0,0,0),
                         (self.width/2-5, self.height/2),
                         (self.width/2+5, self.height/2))
        pygame.draw.line(self.screen, (0,0,0),
                         (self.width/2, self.height/2-5),
                         (self.width/2, self.height/2+5))

        for o in self.Objects:
            o.draw(self)

        pygame.display.flip()

    def addObject(self, obj):
        self.Objects.append(obj)

    def removeObject(self, obj):
        self.Objects.remove(obj)