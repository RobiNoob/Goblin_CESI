from hexagone import *
import pygame, sys
from math import *
from pygame.locals import *

x = 50
y = 50
size = 50
width = sqrt(3)/2*(size*2)

#------------------------------------ off to cub ---------------------------------------------------------
def oddq_to_cube(hex):
    hex.x = hex.col
    hex.z = hex.row - (hex.col - (hex.col&1)) / 2
    hex.y = -hex.x-hex.z

#------------------------------------ cub to axe ---------------------------------------------------------
def cube_to_axial(hex):
    hex.q = hex.x
    hex.r = hex.z

#------------------------------------ hex to pix ---------------------------------------------------------
def hex_to_pixel(hex):
    hex.x = size * 3/2 * hex.q
    hex.y = size * sqrt(3) * (hex.r + hex.q/2)

#------------------------------------ pix to hex ---------------------------------------------------------
def pixel_to_hex(x, y):
    q = x * 2/3 / size
    r = (-x / 3 + sqrt(3)/3 * y) / size
    return (q, r)

#------------------------------------ class grid ---------------------------------------------------------
class grid:

    def __init__(self, DISPLAY):
        pygame.init()
        myfont = pygame.font.SysFont("monospace", 15)
        blue=(0,0,255)
        for col in range(10):
            for row in range(10):
                hex = Hex(col,row)
                oddq_to_cube(hex)
                cube_to_axial(hex)
                hex_to_pixel(hex)
                hexagone(DISPLAY,x+hex.x,y+hex.y,size)
                label = myfont.render(str(hex.col) + ","+str(hex.row), 1, (0,0,0))
                DISPLAY.blit(label, (x+hex.x, y+hex.y))
