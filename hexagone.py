import pygame, sys
from math import *
from pygame.locals import *

#--------------------------------------  Hexagone -----------------------------------------------------
class hexagone:
    def __init__(self,DISPLAY,x,y,size):
        width = sqrt(3)/2*(size*2)
        blue=(0,0,255)
        pygame.draw.polygon(DISPLAY,blue,[
                                           [x+size,y],
                                           [x+size/2,y+width/2],
                                           [x-size/2,y+width/2],
                                           [x-size,y],
                                           [x-size/2,y-width/2],
                                           [x+size/2,y-width/2]
                                       ],1)

    def __new__(self,DISPLAY,x,y,size):
        width = sqrt(3)/2*(size*2)
        blue=(0,0,255)
        pygame.draw.polygon(DISPLAY,blue,[
                                           [x+size,y],
                                           [x+size/2,y+width/2],
                                           [x-size/2,y+width/2],
                                           [x-size,y],
                                           [x-size/2,y-width/2],
                                           [x+size/2,y-width/2]
                                       ],1)

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

    def calcul_distance(x, y):
        distance = sqrt(pow(self.x-x, 2) + pow(self.y - y, 2))
        if distance < 50
            return True
        else
            return False
#-------------------------------------------------------------------------------------------------------------
