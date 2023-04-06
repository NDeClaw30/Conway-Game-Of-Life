from pygame import Vector2
import random

class GoLModel:

    def __init__(self,w,h):
        self._width = w
        self._height = h
        self._grid = [[[0] * self._width] for i in range(self._height)]
    
    def update(self):
        pass
    
    def getSize(self):
        return self._width,self._height
    
    def getGrid(self):
        pass
    
    def setLoc(self,newloc):
        self._loc.x,self._loc.y = newloc[0],newloc[1]