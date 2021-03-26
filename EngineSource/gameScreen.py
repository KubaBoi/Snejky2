"""
uchovává, vykresluje a spravuje objekty
obsuhuje i pygame scene
"""

import pygame
from Engine.camera import Camera
from Engine.vector import Vector

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
        self.camera = Camera(Vector(0,0,0), width/2, height/2)

    def update(self):
        self.camera.update()
        for o in self.Objects:
            o.update()

    def draw(self):
        self.screen.fill((self.color))

        for o in self.Objects:
            o.draw(self.screen, self.camera)

        pygame.display.flip()

    def addObject(self, obj):
        self.Objects.append(obj)

    def removeObject(self, obj):
        self.Objects.remove(obj)