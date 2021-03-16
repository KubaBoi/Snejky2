"""
dedi od Object
rozdeli objekty do shluku a nacita pouze aktivni
"""

from Engine.object import Object

class Scene(Object):
    def __init__(self, position):
        Object.__init__(self, position)