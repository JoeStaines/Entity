import pygame, sys, math, random
from pygame.locals import *


class Entity():
                wW,wH = 800,600
                def __init__(self):
                                
                                self.color = pygame.Color(200,225,255)
                                self.fps = pygame.time.Clock()
                                self.mainRunning = False
                                self.endRunning = False
                                self.halfwidth = Entity.wW/2
                                self.halfheight = Entity.wH/2
                                
                                
                                
                                self.externalFile()
                                self.setDisplay()
                                self.addGroup()

                ################# BEGIN initialize Entity class methods ######################

                def externalFile(self):
                                self.defaultScoreValue = 'No score available'
                                self.fixLoop = True
                                try:
                                    self.scoreFile = open('score.dat','r')
                                    self.scoreFile.close()
                                    
                                except IOError as e:
                                    self.scoreFile = open('score.dat','w')
                                    self.scoreFile.write(self.defaultScoreValue)
                                    self.scoreFile.close()
                    

                def setDisplay(self):
                                self.window = pygame.display.set_mode((Entity.wW,Entity.wH),0,32)
                                self.playArea = pygame.display.get_surface()
                                pygame.display.set_caption("Entity")
                                self.pixels = 0
                                #pygame.mouse.set_visible(0)

                def addGroup(self):
                                self.mainMenuObj = pygame.sprite.Group()
                                self.allPlayer = pygame.sprite.Group()
                                self.allEnemy = pygame.sprite.Group()

                ################ END initialize Entity class methods #######################

                ################ BEGIN main menu methods ####################
                                
                def startGame(self):               
                    
                    self.addMenuObj()

                    
                    
                    while 1:

                        while (self.fixLoop == True):
                            self.readFile()
                            self.fixLoop = False
                        
                        self.drawBackground(True,'mainmenu.jpg')
                        
                        self.highscoreOutput = "The current highscore is {0} points".format(self.highscore)
                        self.outputText(None,120,"E  N  T  I  T  Y",1,(150,210,200),self.halfwidth,100)                     
                        self.outputText(None,32,self.highscoreOutput,1,(190,190,190),self.halfwidth,200)                        
                        self.mainMenuObj.draw(self.playArea)
                                                
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    if (self.playButton.clicked(event.pos) == 1):
                                        self.main()
                                    elif (self.exitButton.clicked(event.pos) == 1):
                                        pygame.quit()
                                        sys.exit()
                                                                                
                        pygame.display.update()
                    

                def addMenuObj(self):
                    self.playButton = Button("playbutton.jpg")
                    self.mainMenuObj.add(self.playButton)
                    
                    self.exitButton = Button("exitbutton.jpg")
                    self.mainMenuObj.add(self.exitButton)
                    
                    self.playButton.rect.center = (self.halfwidth, self.halfheight)
                    self.exitButton.rect.center = (self.halfwidth, self.halfheight+75)

                ################# END main menu methods ##################

                ################# BEGIN main game loop methods ####################

                
                def main(self):
                                
                                self.gameInit()
                                pygame.mouse.set_visible(0)
                                
                                while self.mainRunning:                                                
                                                self.time()
                                                self.levelManager(self.level)
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
                                                
                def gameInit(self):
                            self.mX,self.mY = 0,0
                            self.addSprites()
                            self.mainRunning = True
                            self.bVal = False
                            self.oTime = pygame.time.get_ticks()
                            self.seconds = 0
                            self.level = "1"
                            self.drawAndWait()
                            pygame.mouse.set_visible(0)

                def addSprites(self):
                                self.player = Player((self.halfwidth+100,self.halfheight))
                                self.allPlayer.add(self.player)
                                
                                heightpos = self.halfheight-250
                                for x in range (0,11):
                                        self.enemy = Enemy((100,heightpos), (self.degreesToRadians(self.randDegrees()), random.randrange(6,8))) 
                                        self.allEnemy.add(self.enemy)
                                        heightpos += 50

                                #Enemy((position), (vector))

                def drawAndWait(self):
                    self.drawBackground(False,None)
                    self.allPlayer.draw(self.playArea)
                    self.allEnemy.draw(self.playArea)
                    pygame.display.update()
                    pygame.time.wait(1000)
                                
                def levelManager(self, flag):
                    #if (secs >= 15):
                    #   lvl = 2
                    #   add wall enemys
                    #elif (secs >= 30):
                    #   lvl = 3
                    #   add entity enemy

                    if (flag != "2" and self.seconds >= 5):
                        self.level = "2"
                        #print "LEVEL: {}".format(self.level)
                        self.wallenemy1 = WallEnemy((self.halfwidth+self.halfwidth/2,-50), 2, 1)
                        self.allEnemy.add(self.wallenemy1)
                        self.wallenemy2 = WallEnemy((self.halfwidth-self.halfwidth/2,Entity.wH+50), 2, -1)
                        self.allEnemy.add(self.wallenemy2)

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

                
                    
                                
                ################## END main game loop methods ######################

                ################## BEGIN end screen methods #####################

                def endGame(self):
                    self.endRunning = True
                    
                    self.fixLoop = True
                    
                    self.allEnemy.remove(self.allEnemy.sprites())
                    self.allPlayer.remove(self.allPlayer.sprites())
                    pygame.mouse.set_visible(1)
                    self.checkPlayerPerformance()

                    if(self.highscore == self.defaultScoreValue):
                        self.highscore = self.seconds
                        self.writeFile()

                    elif (int(self.highscore) < self.seconds):
                        self.writeFile()                     

                    while self.endRunning:
                        self.drawBackground(True,'mainmenu.jpg')
                        #self.drawBackground(True,'end.jpg')
                        self.outSeconds = "Your Score is {0}".format(self.seconds)
                        self.outputText(None,74,self.outSeconds,1,(100,120,180),200,150)
                        self.outputText(None,36,self.msgS,1,(150,150,150),300,200)
                        
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    self.mainRunning = False
                                    self.endRunning = False
                        pygame.display.update()

                ################## END end screen methods ###################

                ################## BEGIN misc methods ###################

                def time(self):
                    self.cTime = pygame.time.get_ticks()
                    if (self.cTime >= self.oTime+1000):
                        self.oTime = self.cTime
                        self.seconds += 1
                        #print "SECONDS: ",self.seconds
                                                

                def drawBackground(self,isImage,filename):
                    if (isImage == True):
                        bkgr = pygame.image.load(filename)
                        bkgrRect = bkgr.get_rect()
                        self.playArea.blit(bkgr,bkgrRect)
                    else:
                        self.playArea.fill(self.color)


                def outputText(self,fontType,fontSize,textString,AA,fontColor,xCord,yCord):
                    pygame.font.init() 
                    font = pygame.font.Font(fontType,fontSize)
                    output = font.render(str(textString),AA,(fontColor))
                    outPos = output.get_rect(centerx=xCord,centery=yCord)
                    self.playArea.blit(output,outPos)
                    

                def checkPlayerPerformance(self):
                    self.msgArray = [(8,'Absolutely dreadful'),(16,"Okay, but you need more practice"),(32,"Good, you're getting there!"),(64,'Excellent')]
                    for i in range(0,len(self.msgArray)):
                        self.msgI,self.msgS = self.msgArray[i]
                        if(self.seconds < self.msgI):
                            break;
                        else:
                            self.msgS = 'Heroic mode enabled'

                def writeFile(self):
                        self.scoreFile = open('score.dat','w')
                        self.scoreFile.write(str(self.seconds))
                        self.scoreFile.close()

                def readFile(self):
                        self.scoreFile = open('score.dat','r')
                        self.highscore = self.scoreFile.read()
                        self.scoreFile.close()


                ################## END misc methods ###################


class Enemy(pygame.sprite.Sprite):
                def __init__(self, location, vector):
                        """
                        location :: (int, int) - location to be placed in px
                        vector :: (int, int) - angle and speed
                        """                        
                        pygame.sprite.Sprite.__init__(self)                        
                        self.image = pygame.image.load("player.png").convert_alpha()
                        self.rect = self.image.get_rect()
                        self.vector = vector
                        self.velx = 0
                        self.vely = 0
                        self.position = location
                        self.rect.center = location
                        self.dir = 1
                        self.counter = 0
                        #self.givenAngleForRotation = 20
                        
                        
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
                        

                        #enemy "animation" code
                        self.counter+=1
                        """
                        if (self.counter >= 2):
                            self.image = self.animateEnemy(self.image,45)
                            #self.image,self.rect = self.animateEnemy('enemy_.png',15)
                            self.counter = 0
                        #end enemy animation code - timer not necessary as it will go at fps rate, added for slower animation
                        """
                        self.rect = self.rect.move(self.velx, self.vely)
                        #self.rect = self.move(self.vector)
                        #self.rect.center = self.position


                def animateEnemy(self,imageToRotate,angleToRotateBy):
                    self.rImage = pygame.transform.rotate(imageToRotate,angleToRotateBy)
                    self.oRect = imageToRotate.get_rect()
                    self.rRect = self.oRect.copy()
                    self.rRect.center = self.rImage.get_rect().center
                    self.rImage = self.rImage.subsurface(self.rRect).copy()
                    return self.rImage
                   


class WallEnemy(pygame.sprite.Sprite):

    def __init__(self, location, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wallenemy.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.speed = speed*direction
        self.inArea = False

    def checkInArea(self):
        if ((self.rect.centerx >= 1 and self.rect.centery >= 1) and (self.rect.centerx <= Entity.wW-1 and self.rect.centery <= Entity.wH-1)):
            self.inArea = True

    def checkEdge(self):
        if (self.inArea):
            if (self.rect.centery <= 0):
                #self.rect.centery = 1
                self.speed *= -1
            elif (self.rect.centery >= Entity.wH):
                #self.rect.centery = Entity.wH-1
                self.speed *= -1

    def update(self):
        self.checkInArea()
        self.checkEdge()
        self.rect = self.rect.move(0,self.speed)


class Player(pygame.sprite.Sprite):
    
        def __init__(self,location):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load('sprite.png').convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = location
                        self.position = location
                        self.health = 25
                        #self.aniImages = []
                        #self.noOfFrames = 10
                        #self.rotateBy = 360/self.noOfFrames
                        #self.x = 0
                        #self.oAniImages = pygame.image.load('1.png').
                        
                    
                        #for i in range(0,self.noOfFrames):
                            #self.aniImages.append(pygame.transform.rotate(self.image,self.rotateBy))
                            #self.rotateBy += self.rotateBy
                        #for i in range(0,10):
                            #print self.aniImages[i]

                        
    

        def update(self):
                        self.rect.center = self.position
                        #self.image = self.aniImages[self.x]
                        #self.x = (self.x + 1) % 10
                        
        def move(self,mX,mY):
                                                                self.position = (mX,mY)

        

class Button(pygame.sprite.Sprite):

    def __init__(self, src):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(src).convert()
      self.rect = self.image.get_rect()

    def clicked(self,pos):
        if (self.rect.left < pos[0] < self.rect.right) and (self.rect.top < pos[1] < self.rect.bottom):
            return 1              
                                                                
if __name__ == "__main__":
                        Entity().startGame()
