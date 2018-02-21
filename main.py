import pygame, sys
from math import *
from pygame.locals import *
from grid import *

def main():
    pygame.init()
    DISPLAY=pygame.display.set_mode((488,825),0,32)
    WHITE=(255,255,255)
    DISPLAY.fill(WHITE)
    fond = pygame.image.load("goblin_map1.jpg")
    DISPLAY.blit(fond, (0,0))



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
