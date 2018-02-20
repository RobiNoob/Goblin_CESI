import pygame, sys
from math import *
from pygame.locals import *
from grid import *

def main():
    pygame.init()
    DISPLAY=pygame.display.set_mode((1800,900),0,32)
    WHITE=(255,255,255)
    DISPLAY.fill(WHITE)

    grid(DISPLAY)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                hex = pixel_to_hex(pos[0], pos[1])
                unHexagone = hexagone(DISPLAY, pos[0], pos[1], 50)
                print(str(pos[0])+" , "+str(pos[1]))
        pygame.display.update()
main()
