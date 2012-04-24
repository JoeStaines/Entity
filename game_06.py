import pygame, sys, math
from pygame.locals import *


class Entity():
		wW, wH = 450, 450

		def __init__(self):
				self.mX,self.mY = 0,0
				self.color = pygame.Color(50,100,150)
				self.enemyUpdateTime = 0
				
				self.setDisplay()
				self.addGroup()
				self.addSprites()
				
		def setDisplay(self):
				self.window = pygame.display.set_mode((Entity.wW,Entity.wH),0,32)
				self.playArea = pygame.display.get_surface()
				pygame.display.set_caption("Entity")
				pygame.mouse.set_visible(0)

		def degreesToRadians(self, degrees):
			return degrees * (math.pi / 180)
				
		def addSprites(self):
				self.player = Player((self.mX,self.mY))
				self.allPlayer.add(self.player)
				
				#Enemy((position), (vector))
				self.enemy = Enemy((100,100), (self.degreesToRadians(200), 10) )
				self.allEnemy.add(self.enemy)

		def addGroup(self):
				self.allPlayer = pygame.sprite.Group()
				self.allEnemy = pygame.sprite.Group()

		def main(self):
				while 1:
						self.playArea.fill(self.color)
						self.player.move(self.mX,self.mY)
						self.allPlayer.update()
						
						if (self.enemyUpdateTime >=50):
							self.allEnemy.update()
							self.enemyUpdateTime = 0
						else:
							self.enemyUpdateTime += 1
						
						self.allPlayer.draw(self.playArea)
						self.allEnemy.draw(self.playArea)

						for event in pygame.event.get():
								if event.type == QUIT:
										pygame.quit()
										sys.exit()
								elif event.type == MOUSEMOTION:
										self.mX,self.mY = event.pos
										
						pygame.display.update()

class Enemy(pygame.sprite.Sprite):
		def __init__(self, location, vector):
			"""
			location :: (int, int) - location to be placed in px
			vector :: (int, int) - angle and speed
			"""
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("enemy.png")
			self.rect = self.image.get_rect()
			
			self.vector = vector
			self.position = location
			self.rect.center = location
			self.dir = 1
			
		def checkEdge(self):
			if self.position[0] >= Entity.wW:
				self.dir = -1
			elif self.position[0] <= 0:
				self.dir = 1
			
		def move(self, vector):
			angle, speed = vector
			(dx, dy) = (math.cos(angle)*speed, math.sin(angle)*speed)
			print (dx, dy)
			return self.rect.move(dx, dy)
			
		def update(self):
			self.rect = self.move(self.vector)
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
