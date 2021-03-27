import pygame

from Engine.gameScreen import GameScreen

class Engine:
    def __init__(self):
        self.gameScreen = GameScreen()
        self.clock = pygame.time.Clock()

    def update(self):
        self.clock = pygame.time.Clock()

        self.gameScreen.update()
        self.draw()

        pygame.event.pump()

    def draw(self):
        self.gameScreen.draw()

    def addObject(self, obj):
        self.gameScreen.addObject(obj)
    
    def removeObject(self, obj):
        self.gameScreen.removeObject(obj)