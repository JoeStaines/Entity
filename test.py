import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((640,480))
fpsClock = pygame.time.Clock()
whiteColour = pygame.Color(255, 255, 255)
screen = pygame.display.get_surface()

mousex, mousey = 0, 0
colourkey = (255,0,255)

ball = pygame.image.load("ball.gif").convert()
ball.set_colorkey(colourkey)

screen.fill(whiteColour)
screen.blit(ball, (0,0))

pygame.mouse.set_visible(0)

while True:
	ballRect = ball.get_rect()
	ballRect.center = (mousex, mousey)
	
	screen.fill(whiteColour)
	screen.blit(ball, ballRect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
	
	pygame.display.update()
	fpsClock.tick(60)
