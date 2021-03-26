import pygame

from Engine.gameScreen import GameScreen

class Engine:
    def __init__(self):
        self.gameScreen = GameScreen(color=(255,0,0))

    def update(self):
        self.gameScreen.update()
        self.draw()

    def draw(self):
        self.gameScreen.draw()

    def addObject(self, obj):
        self.gameScreen.addObject(obj)
    
    def removeObject(self, obj):
        self.gameScreen.removeObject(obj)