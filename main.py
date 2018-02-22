import pygame, sys
from math import *
from pygame.locals import *
from grid import *

def main():
    pygame.init()
    screen = pygame.display
    DISPLAY=screen.set_mode((1310,929),0,32)
    screen.set_caption('Goblin Dwarf Star')
    WHITE=(255,255,255)
    DISPLAY.fill(WHITE)
    fond = pygame.image.load("carte.jpg")
    DISPLAY.blit(fond, (0,0))



    g = grid(DISPLAY)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                g.onClick(pos[0],pos[1], DISPLAY, fond)
        screen.update()
main()
