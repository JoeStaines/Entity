import pygame, sys, math
from pygame.locals import *


class Entity():
		wW, wH = 450, 450

		def __init__(self):
				self.mX,self.mY = 0,0
				self.color = pygame.Color(50,100,150)
				
				self.setDisplay()
				self.addGroup()
				self.addSprites()
				
		def setDisplay(self):
				self.window = pygame.display.set_mode((Entity.wW,Entity.wH),0,32)
				self.playArea = pygame.display.get_surface()
				pygame.display.set_caption("Entity")
				pygame.mouse.set_visible(0)

		def addSprites(self):
				self.player = Player((self.mX,self.mY))
				self.allSprites.add(self.player)
				self.enemy = Enemy((100,100))
				self.allSprites.add(self.enemy)

		def addGroup(self):
				self.allSprites = pygame.sprite.Group()

		def main(self):
				while 1:
						self.playArea.fill(self.color)
						self.player.move(self.mX,self.mY)
						self.allSprites.update()
						self.allSprites.draw(self.playArea)

						for event in pygame.event.get():
								if event.type == QUIT:
										pygame.quit()
										sys.exit()
								elif event.type == MOUSEMOTION:
										self.mX,self.mY = event.pos
										
						pygame.display.update()

class Enemy(pygame.sprite.Sprite):
		def __init__(self, location):
			"""
			location :: (int, int) - location to be placed in px
			"""
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("enemy.png")
			self.rect = self.image.get_rect()
			
			self.position = location
			self.rect.center = location
			self.dir = 1
			
		def checkEdge(self):
			if self.position[0] >= Entity.wW:
				self.dir = -1
			elif self.position[0] <= 0:
				self.dir = 1
			
		def move(self):
			(dx, dy) = (math.cos(0.2)*10, math.sin(0.2)*10)
			print (dx, dy)
			return self.rect.move(dx, dy)
			
		def update(self):
			self.rect = self.move()
			#self.rect.center = self.position
						
class Player(pygame.sprite.Sprite):
        def __init__(self,location):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("sprite.png")
                self.rect = self.image.get_rect()
                self.rect.center = location
                self.position = location
                #set sprite to mouse position

        def update(self):
                self.rect.center = self.position

                
        def move(self,mX,mY):
                self.position = (mX,mY)                
                
if __name__ == "__main__":
        Entity().main()
