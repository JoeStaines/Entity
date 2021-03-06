import pygame, sys, math, random
from pygame.locals import *


class Entity():
                wW,wH = 800,600
                def __init__(self):
                                
                                self.color = pygame.Color(50,100,150)
                                self.fps = pygame.time.Clock()
                                self.setDisplay()
                                self.addGroup()
                                

                def gameInit(self):
                            self.mX,self.mY = 0,0
                            self.addSprites()
                            self.bVal = False
                            self.oTime = pygame.time.get_ticks()
                            self.seconds = 0
                                
                def setDisplay(self):
                                self.window = pygame.display.set_mode((Entity.wW,Entity.wH),0,32)
                                self.playArea = pygame.display.get_surface()
                                pygame.display.set_caption("Entity")
                                #pygame.mouse.set_visible(0)

                def degreesToRadians(self, degrees):
                        return degrees * (math.pi / 180)

                        
                def checkCollide(self):
                                self.bVal = pygame.sprite.spritecollideany(self.player,self.allEnemy)
                                if(self.bVal != None):
                                                    self.player.health -= 1
                                                    #print "Collision Detected, Health: ",self.player.health
                                if(self.player.health <= 0):
                                    self.endGame()

                                                
                def randDegrees(self):
                        deadzones = range(0,6)
                        deadzones += range(85,96)
                        deadzones += range(175,186)
                        deadzones += range(265,276)
                        deadzones += range(355,360)
                        rand = 0
                        
                        while (rand in deadzones):
                                rand = random.randrange(0,359)
                        
                        return rand
                

                def addSprites(self):
                                self.player = Player((self.mX,self.mY))
                                self.allPlayer.add(self.player)
                                

                                for x in range (0,4):
                                        self.enemy = Enemy((100,100), (self.degreesToRadians(self.randDegrees()), random.randrange(5,15))) 
                                        self.allEnemy.add(self.enemy)
                                                                

                                #Enemy((position), (vector))
                                


                def addGroup(self):
                                self.allPlayer = pygame.sprite.Group()
                                self.allEnemy = pygame.sprite.Group()

                def time(self):
                    self.cTime = pygame.time.get_ticks()
                    if (self.cTime >= self.oTime+1000):
                        self.oTime = self.cTime
                        self.seconds += 1
                        print "SECONDS: ",self.seconds

                def startGame(self):
                    while 1:
                        self.drawBackground(True,'bkgr.jpg')
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                b1,b2,b3= pygame.mouse.get_pressed()
                                if (b1 == True):
                                   self.main()

                        pygame.display.update()

                def drawBackground(self,isImage,filename):
                    if (isImage == True):
                        bkgr = pygame.image.load(filename)
                        bkgrRect = bkgr.get_rect()
                        self.playArea.blit(bkgr,bkgrRect)
                    else:
                        self.playArea.fill(self.color)

                def endGame(self):
                    self.allEnemy.remove(self.allEnemy.sprites())
                    self.allPlayer.remove(self.allPlayer.sprites())
                    pygame.mouse.set_visible(1)

                    while 1:
                        self.drawBackground(True,'end.jpg')
                        self.outSeconds = "SCORE {0}".format(self.seconds)
                        self.outputText(None,30,self.outSeconds,1,(10,10,10),350,300)
                        
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    self.startGame()
                        pygame.display.update()


                def outputText(self,fontType,fontSize,textString,AA,fontColor,xCord,yCord):
                    pygame.font.init() 
                    font = pygame.font.Font(fontType,fontSize)
                    output = font.render(str(textString),AA,(fontColor))
                    outPos = output.get_rect(centerx=xCord,centery=yCord)
                    self.playArea.blit(output,outPos)


                def main(self):
                                self.gameInit()
                                pygame.mouse.set_visible(0)                    
                                while 1:
                                                self.time()
                                                self.drawBackground(False,None)
                                                self.player.move(self.mX,self.mY)
                                                self.allPlayer.update()
                                                self.allEnemy.update()
                                                self.checkCollide()
                                                self.allPlayer.draw(self.playArea)
                                                self.allEnemy.draw(self.playArea)
                                                
                                                for event in pygame.event.get():
                                                                                if event.type == QUIT:
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                elif event.type == MOUSEMOTION:
                                                                                    self.mX,self.mY = event.pos
                                                                                                                
                                                pygame.display.update()
                                                self.fps.tick(60)                               


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
                        self.velx = 0
                        self.vely = 0
                        
                        self.position = location
                        self.rect.center = location
                        self.dir = 1
                        
                        self.calcAngle(self.vector)

                        #calc angle only once on create
                        
                def calcAngle(self, vector):
                        angle, speed = vector
                        (self.velx, self.vely) = (self.myRound(math.cos(angle)*speed), self.myRound(math.sin(angle)*speed))
                        
                def myRound(self, dVal):
                        frac,whole = math.modf(dVal)
                        if(frac>=0.5):
                                whole+=1
                        return whole
                
                def checkEdge(self):
                        if self.rect.top <= 0 or self.rect.bottom >= Entity.wH:
                                self.bounce('y')
                        elif self.rect.left <= 0 or self.rect.right >= Entity.wW:
                                self.bounce('x')
                
                def bounce(self, axis):
                        if axis == 'x':
                                self.velx *= -1
                        elif axis == 'y':
                                self.vely *= -1
                        else:
                                print "Error bouncing"
                
                def update(self):
                        self.checkEdge()

                        #print self.vely, self.rect.top


                        self.rect = self.rect.move(self.velx, self.vely)
                        #self.rect = self.move(self.vector)
                        #self.rect.center = self.position
                        
class Player(pygame.sprite.Sprite):
    
        def __init__(self,location):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load("sprite.png").convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = location
                        self.position = location
                        self.health = 5


        def update(self):
                        self.rect.center = self.position

        def move(self,mX,mY):
                        self.position = (mX,mY)                
                                                                
if __name__ == "__main__":
                        Entity().startGame()
