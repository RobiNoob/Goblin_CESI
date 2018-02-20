import pygame, sys
from math import *
from pygame.locals import *
from grid import *

def main():
    pygame.init()
    DISPLAY=pygame.display.set_mode((1800,900),0,32)
    WHITE=(255,255,255)
    DISPLAY.fill(WHITE)

    g = grid(DISPLAY)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                g.calcul_point(pos[0],pos[1], DISPLAY)
        pygame.display.update()
main()
