import pygame, sys
from pygame.locals import *

"""
def main():
    pygame.init()
    window = pygame.display.set_mode((400,400),0,32)
    screen = pygame.display.get_surface()
    color = pygame.Color(20,40,80)
    mx,my = 0,0
    obj = pygame.image.load('sprite.png').convert_alpha()
    screen.fill(color)
    pygame.mouse.set_visible(0)
    
    while 1:
        objR = obj.get_rect()
        objR.center = (mx,my)

        screen.fill(color)
        screen.blit(obj,objR)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mx,my = event.pos
        pygame.display.update()
    
"""    


def main():
	#some shit
	pygame.init()
	

class player(pygame.sprite.Sprite):
	def __init__(self,setIniLoc):
		



main()
        
