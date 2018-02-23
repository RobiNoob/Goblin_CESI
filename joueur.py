import pygame, sys
from pygame.locals import *
from hexagone import *

x = 77
y = 72
size = 70
width = sqrt(3)/2*(size*2)

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

class joueur:

    typeJoueur = 0
    pointMouvement = 0
    modificateurMorale = 0
    nombreUnite = 0
    armure = 0
    col = 0
    row = 0

    def __init__ (self, typeJoueur, pointMouvement, modificateurMorale, nombreUnite, armure, col, row):
        self.typeJoueur = typeJoueur
        self.pointMouvement = pointMouvement
        self.modificateurMorale = modificateurMorale
        self.nombreUnite = nombreUnite
        self.armure= armure
        self.col = col
        self.row = row


    def drawJoueur(self, DISPLAY):
        img = pygame.image.load("Joueur/King_Goblin.png")
        hexa = Hex(self.col, self.row)
        oddq_to_cube(hexa)
        cube_to_axial(hexa)
        hex_to_pixel(hexa)
        DISPLAY.blit(img, (hexa.x+40, hexa.y+30))

