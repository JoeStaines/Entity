import pygame, sys, math, random
from pygame.locals import *


class Entity():
        wW,wH = 450,450
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

        def checkCollide(self):
                        self.bVal = pygame.sprite.collide_rect(self.player,self.enemy)
                        if(self.bVal == 1):
                                self.player.health-=1
                                #or any other action

        def main(self):
                        while 1:
                                        self.playArea.fill(self.color)
                                        self.player.move(self.mX,self.mY)
                                        self.allSprites.update()
                                        self.allSprites.draw(self.playArea)
                                        self.checkCollide()
                                        print "HEALTH",self.player.health
                                        print "COLLIDE?",self.bVal
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
                        (dx, dy) = (self.myRound(math.cos(0.4)*1), self.myRound(math.sin(0.4)*1))
                        return self.rect.move(dx,dy)

                def myRound(self, dVal):
                        frac,whole = math.modf(dVal)
                        if(frac>=0.5):
                                whole+=1
                        return whole
                
                def update(self):
                        self.rect = self.move()
                        #self.rect.center = self.position
                                                
class Player(pygame.sprite.Sprite):
        
        def __init__(self,location):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("sprite.png").convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.center = location
                self.position = location
                self.health = 100

        def update(self):
                self.rect.center = self.position

        def move(self,mX,mY):
                self.position = (mX,mY)                
                
if __name__ == "__main__":
        Entity().main()
