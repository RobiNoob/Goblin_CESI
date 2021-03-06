import pygame, sys
from math import *
from pygame.locals import *

#--------------------------------------  Hexagone -----------------------------------------------------
class hexagone:
    def __init__(self,DISPLAY,x,y,size):
        width = sqrt(3)/2*(size*2)
        blue=(0,0,0)
        pygame.draw.polygon(DISPLAY,blue,[
                                           [x+size,y],
                                           [x+size/2,y+width/2],
                                           [x-size/2,y+width/2],
                                           [x-size,y],
                                           [x-size/2,y-width/2],
                                           [x+size/2,y-width/2]
                                       ],2)

    def __new__(self,DISPLAY,x,y,size):
        width = sqrt(3)/2*(size*2)
        blue=(0,0,0)
        pygame.draw.polygon(DISPLAY,blue,[
                                           [x+size,y],
                                           [x+size/2,y+width/2],
                                           [x-size/2,y+width/2],
                                           [x-size,y],
                                           [x-size/2,y-width/2],
                                           [x+size/2,y-width/2]
                                       ],2)

class Hex:
    col = 0
    row = 0
    q = 0
    r = 0
    x = 0
    y = 0
    z = 0
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def calcul_distance(self, x, y):
        distance = sqrt(pow((self.x+50)-x, 2) + pow((self.y+50) - y, 2))
        if distance < 68:
            return True
        else:
            return False
#-------------------------------------------------------------------------------------------------------------
