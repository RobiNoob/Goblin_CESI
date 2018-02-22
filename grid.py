from hexagone import *
import pygame, sys
from math import *
from pygame.locals import *
from joueur import *

x = 77
y = 72
size = 70
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

oddq_directions = [
   [ Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
     Hex(-1, -1), Hex(-1,  0), Hex( 0, +1) ],
   [ Hex(+1, +1), Hex(+1,  0), Hex( 0, -1),
     Hex(-1,  0), Hex(-1, +1), Hex( 0, +1) ]
]

def oddq_offset_neighbor(hex, direction):
    parity = hex.col & 1
    dir = oddq_directions[parity][direction]
    hexa  = Hex(hex.col + dir.col, hex.row + dir.row)
    oddq_to_cube(hexa)
    cube_to_axial(hexa)
    hex_to_pixel(hexa)
    return hexa

#------------------------------------ class grid ---------------------------------------------------------
class grid:


    tabHex = []
    i = 12
    j = 7

    # plaine = 0 def
    # foret = 1
    # ville = 2
    # route = 3
    # montagne = 4
    # lac = 5
    # cave = 6

    terrain = [
        ((3,0),1),((3,1),1),((2,4),1),((2,5),1),((6,6),1),
        ((1,1),2),((1,2),2),((2,6),2),((5,0),2),((6,0),2),((6,1),2),((8,5),2),((8,6),2),
        ((3,2),3),((4,2),3),((5,1),3),((2,3),3),((2,4),3),((2,5),3),((3,5),3),((3,4),3),
        ((4,4),3),((5,3),3),((6,2),3),((6,3),3),((6,4),3),((6,5),3),((7,5),3),
        ((9,0),4),((10,0),4),((10,1),4),((10,2),4),((10,3),4),((10,4),4),((11,1),4),((11,2),4),((11,3),4),
        ((3,3),5),((9,2),6),
              ]

    # route = 1
    # rivier = 2
    # pont = 3

    arc = [
        ((3,2),(4,2),1),((4,2),(5,1),1),((2,2),(2,3),1),((2,4),(2,5),1),((3,5),(3,4),1),((3,4),(4,4),1),
        ((4,4),(5,3),1),((5,3),(6,3),1),((6,2),(6,3),1),((6,3),(6,4),1),((6,4),(6,5),1),((6,5),(7,5),1),
        ((0,2),(0,3),2),((1,2),(0,3),2),((1,2),(1,3),2),((2,3),(1,3),2),((3,2),(4,3),2),((4,2),(4,3),2),
        ((4,2),(5,2),2),((5,1),(5,2),2),((5,1),(6,2),2),((4,4),(4,5),2),((5,4),(4,5),2),((4,5),(5,4),2),
        ((4,6),(5,5),2),((4,6),(5,6),2),((10,6),(11,6),2),((10,6),(11,5),2),((10,5),(11,5),2),((11,4),(11,5),2),
        ((2,3),(2,4),3),
    ]

    unJoueur = joueur(1, 10, 2, 12, 2, 0, 0)

    def __init__(self, DISPLAY):
        pygame.init()
        self.unJoueur.drawJoueur(DISPLAY)
        myfont = pygame.font.SysFont("monospace", 15)
        blue=(0,0,255)
        for col in range(self.i):
            for row in range(self.j):
                hex = Hex(col,row)
                oddq_to_cube(hex)
                cube_to_axial(hex)
                hex_to_pixel(hex)
                self.tabHex.append(hex)
                #hexagone(DISPLAY,x+hex.x,y+hex.y,size)
                label = myfont.render(str(hex.col) + ","+str(hex.row), 1, (255,255,255))
                DISPLAY.blit(label, (x+hex.x, y+hex.y))

    def onClick(self, x, y, DISPLAY, fond):
        for hexa in self.tabHex:
            if hexa.calcul_distance(x, y) == True:
                red = (255, 0, 0)
                green = (0, 255, 0)
                pygame.draw.rect(DISPLAY, red, [hexa.x+38, hexa.y+44, 25, 25])
                self.updateGrid(fond, DISPLAY)
                self.unJoueur.col = hexa.col
                self.unJoueur.row = hexa.row
                self.unJoueur.drawJoueur(DISPLAY)
                for i in range (0, 6):
                    hexa2 = oddq_offset_neighbor(hexa, i)
                    if hexa2.col >= 0 and hexa2.col < self.i:
                        if hexa2.row >= 0 and hexa2.row < self.j:
                            pygame.draw.rect(DISPLAY, green, [hexa2.x+38, hexa2.y+44, 25, 25])
                break

    def updateGrid(self, fond, DISPLAY):
        DISPLAY.blit(fond, (0,0))
        for hexa in self.tabHex:
            myfont = pygame.font.SysFont("monospace", 15)
            label = myfont.render(str(hexa.col) + ","+str(hexa.row), 1, (255,255,255))
            DISPLAY.blit(label, (x+hexa.x, y+hexa.y))
