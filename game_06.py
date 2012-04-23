import pygame, sys
from pygame.locals import *
    	

class EnemyObject(pygame.sprite.Sprite):
		def __init__(self, location)
			"""
			location :: (int, int) - location to be placed in px
			"""
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("enemy.png")
			self.rect = self.image.get_rect()
			
			self.position = location
			self.rect.center = location
			
		def update(self)
			self.position = (self.position[0]+1, self.position[1])
			self.rect.center = self.position
			