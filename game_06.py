import pygame, sys
from pygame.locals import *

class Entity():
        def __init__(self):
                self.mX,self.mY = 0,0
                self.color = pygame.Color(200,240,60)
                self.setDisplay()
                self.addGroup()
                self.addSprites()
                
        
        def setDisplay(self):
                self.window = pygame.display.set_mode((400,400),0,32)
                self.playArea = pygame.display.get_surface()
                pygame.display.set_caption("Entity")
                pygame.mouse.set_visible(0)

        def addSprites(self):
                self.player = Player((self.mX,self.mY))
                self.allSprites.add(self.player)

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
        
