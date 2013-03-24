 # Amy (Zhao) Yu
# A simplified version of the classic game Asteroids

import pygame 
from pygame.locals import *   
from copy import copy
import math, random

GAME_WIDTH=640
GAME_HEIGHT=480


class Asteroid: 
    def __init__(self, background, screen, size, x, y):
        if size == 1:
            self.size = size
            self.image = pygame.image.load("asteroid_small.bmp")
            self.image.set_colorkey(self.image.get_at((0,0)), RLEACCEL)
            self.image.convert()
        elif size == 2:
            self.size = size
            self.image = pygame.image.load("big_asteroid.bmp")
            self.image.set_colorkey(self.image.get_at((0,0)), RLEACCEL)
            self.image.convert()
        else:
            print "Invalid size"
        
        self.rect=self.image.get_rect()
        self.background=background
        self.screen=screen
    
        self.speed=1.5
        self.angle=random.random()*2*math.pi
        # keep a floating point true position and and integer approximation
        #self.fx=float(self.rect.centerx)
        #self.fy=float(self.rect.centery)
        if (size == 1):
            self.fx = x
            self.fy = y
        elif (size == 2):
            self.fx = random.randint(0,GAME_WIDTH)*random.randrange(0,2)
            self.fy = random.randint(0,GAME_HEIGHT)*random.randrange(0,2)
            if (self.fx != 0) and (self.fy != 0):
                if (self.fx <= self.fy):
                    self.fx = GAME_WIDTH
                elif (self.fx > self.fy):
                    self.fy = GAME_HEIGHT
        
        
        print "Start location: (" + str(self.fx) + ", " + str(self.fy) + ")"
        print "Start angle: " + str(self.angle)
    
    def update(self, asteroids, shots):
        dirtyRects=[copy(self.rect)]
        # move the asteroid
        self.fx+=self.speed*math.cos(self.angle)
        self.fy+=self.speed*math.sin(self.angle)
        
        self.rect.centerx=int(self.fx)
        self.rect.centery=int(self.fy)

        # check for collisions with screen edge
        if self.fx > GAME_WIDTH : self.fx = 0
        elif self.fx < 0:self.fx = GAME_WIDTH
        if self.fy > GAME_HEIGHT : self.fy = 0
        elif self.fy < 0:self.fy = GAME_HEIGHT      
        
        # check for collisions with shot
        # if self.size = 1, then destroy
        # if self.size = 2, then break into three smaller asteroids
        
        for s in shots:
            if self.rect.colliderect(s.rect):
                print "Self is " + str(self)
                if self.size == 2:
                    print "Asteroids before removing self " + str(asteroids)
                    if self in asteroids:
                        asteroids.remove(self)
                        dirtyRects.append(s.rect)
                        shots.remove(s)
                        asteroids.append(Asteroid(self.background, self.screen, 1, self.fx, self.fy))
                        asteroids.append(Asteroid(self.background, self.screen, 1, self.fx, self.fy))
                        asteroids.append(Asteroid(self.background, self.screen, 1, self.fx, self.fy))
                    print "Asteroids after removing self " + str(asteroids)
                elif self.size == 1:
                    print "Asteroids before removing self " + str(asteroids)
                    dirtyRects.append(self.image.get_rect())
                    if self in asteroids:
                        asteroids.remove(self)
                        dirtyRects.append(s.rect)
                        shots.remove(s)
                    print "Asteroids after removing self " + str(asteroids)
        return dirtyRects
    
        
    
    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)
        return [copy(self.rect)]

class Shot:
    
    def __init__(self, background, screen, angle, x, y):
        self.image = pygame.image.load("shot.bmp")
        self.image.set_colorkey(self.image.get_at((0,0)), RLEACCEL)
        self.image.convert()
        self.rect=self.image.get_rect()
        self.background = background
        self.screen = screen
        self.angle = angle
        self.speed = 4.00
        self.fx = x
        self.fy = y
        self.time = 0
        
    def update(self):
        dirtyRects=[copy(self.rect)]
        self.fx+=self.speed*math.cos(self.angle)
        self.fy+=self.speed*math.sin(self.angle)
        
        self.rect.centerx=int(self.fx)
        self.rect.centery=int(self.fy)
        self.time += 1
        
        if self.fx > GAME_WIDTH : self.fx = 0
        elif self.fx < 0:self.fx = GAME_WIDTH
        if self.fy > GAME_HEIGHT : self.fy = 0
        elif self.fy < 0:self.fy = GAME_HEIGHT  
        
        return dirtyRects
    
    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)
        return [copy(self.rect)]
        
class Ship:

    def __init__(self, background, screen):
        self.image=pygame.image.load("falcon.bmp")
        self.image.set_colorkey(self.image.get_at((0,0)), RLEACCEL)
        self.image.convert()
        self.rect=self.image.get_rect()
        self.screenRect=screen.get_rect()
        self.rect.centerx=self.screenRect.centerx
        self.rect.centery=self.screenRect.centery
        self.background=background
        self.screen=screen
        self.speed=0.00
        self.angle = 0.00
        self.rot = 0
        
        # keep a floating point true position and and integer approximation
        self.fx=float(self.rect.centerx)
        self.fy=float(self.rect.centery)
        
    def get_input(self, event, asteroids, shots):
        oldrect = None
        if (event.type == pygame.KEYUP) or (event.type == pygame.KEYUP): 
            print event
            if (event.key == K_LEFT):
                self.angle -= math.radians(20)
                self.rot -= 20
            if (event.key == K_RIGHT):
                self.angle += math.radians(20)
                self.rot += 20
            if (event.key == K_UP):
                self.speed += 4.0
            if (event.key == K_DOWN):
                self.speed *= .90
            if (event.key == K_SPACE):
                print "fired shot"
                # change 
                shots.append(Shot(self.background, self.screen, self.angle, self.fx + 45*math.cos(math.radians(self.rot)), self.fy+ 45*math.sin(math.radians(self.rot))))
            if (event.key == K_ESCAPE):
                oldrect = [copy(self.rect)]
                self.fx = random.randint(0,GAME_WIDTH)
                self.fy = random.randint(0,GAME_HEIGHT)
                #new code
                
                self.rect.centerx=self.fx
                self.rect.centery=self.fy
                for s in shots:
                    for a in asteroids:
                        while(self.rect.colliderect(a.rect) or self.rect.colliderect(s.rect)):
                            self.fx = random.randint(0,GAME_WIDTH)
                            self.fy = random.randint(0,GAME_HEIGHT)
                            self.rect.centerx=self.fx
                            self.rect.centery=self.fy
                
        return oldrect
                
                
    def update(self):
        dirtyRects=[copy(self.rect)]

        self.fx+=self.speed*math.cos(self.angle)
        self.fy+=self.speed*math.sin(self.angle)
        
        self.rect.centerx=int(self.fx)
        self.rect.centery=int(self.fy)

        if self.fx > GAME_WIDTH : self.fx = 0
        elif self.fx < 0:self.fx = GAME_WIDTH
        if self.fy > GAME_HEIGHT : self.fy = 0
        elif self.fy < 0:self.fy = GAME_HEIGHT 
        
        
        print "Angle: " + str(self.angle) 
        print "Speed: " + str(self.speed)
        print "Location: (" + str(self.fx) + ", " + str(self.fy) + ")"
        
        self.speed *= .99
        return dirtyRects
    
    def draw(self):
        ShipPicRotated = pygame.transform.rotozoom(self.image, self.rot, 0.85)
        ShipPicRotated = pygame.transform.flip(ShipPicRotated, 1, 0)
        height = ShipPicRotated.get_height()/2.0
        width = ShipPicRotated.get_width()/2.0
        tmp_pos = [int(self.rect.centerx-width),int(self.rect.centery-height)]
        self.screen.blit(ShipPicRotated, (tmp_pos[0],tmp_pos[1])) 
        return [copy(self.rect)]


class simpleGame:

    def __init__(self):
        pygame.init() 
        pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("ASTEROIDS")
        self.screen=pygame.display.get_surface()
        self.bgSurface=self.drawBackground(pygame.image.load("background.jpg").convert())
        self.screen.blit(self.bgSurface, (0,0))
        self.asteroids = [Asteroid(self.bgSurface, self.screen, 2, 0, 0), Asteroid(self.bgSurface, self.screen, 2, 0, 0)]
        self.shots = []
        self.level = 1;
        self.ship = Ship(self.bgSurface, self.screen)
        pygame.display.update()
        self.clock = pygame.time.Clock()
    
    def updateBackground(self, dirtyRects):
        for rect in dirtyRects:
            self.screen.blit(self.bgSurface, rect, rect)
        
    def eventLoop(self):
        global Explosion
        while 1:
            dirtyRects=[]
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                else:
                    x = self.ship.get_input(event, self.asteroids, self.shots)
                    if (x != None):
                        dirtyRects.extend(x)
            for a in self.asteroids:
                dirtyRects.extend(a.update(self.asteroids, self.shots))
            dirtyRects.extend(self.ship.update())
            for s in self.shots:
                dirtyRects.extend(s.update())
                if (self.ship.rect.colliderect(s.rect) and s.time > 10):
                    print "You hit a shot!"
                    return
            self.updateBackground(dirtyRects)
            for a in self.asteroids:
                dirtyRects.extend(a.draw())
                if self.ship.rect.colliderect(a.rect): 
                    print "You hit an asteroid!"
                    return
            dirtyRects.extend(self.ship.draw())
            for s in self.shots:
                if s.time > 90:
                    dirtyRects.append(s.rect)
                    self.shots.remove(s)  
                else:
                    dirtyRects.extend(s.draw()) 
            pygame.display.update(dirtyRects)
            self.clock.tick(60)
            # Check if level is done, if all asteroids destroyed, then introduce new level
            if len(self.asteroids) == 0:
                self.level += 1
                for i in range(0, self.level+1):
                    self.asteroids.append(Asteroid(self.bgSurface, self.screen, 2, 0, 0))
    
    def drawBackground(self, bgTile):
        bgTileRect=bgTile.get_rect()
        tileWidth=bgTileRect.width
        tileHeight=bgTileRect.height

        background=pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

        x=0
        while (x<GAME_WIDTH):
            y=0
            while (y<GAME_HEIGHT):
                background.blit(bgTile, (x,y))
                y+=tileHeight
            x+=tileWidth
        return background
    

if __name__ == '__main__':
    myGame = simpleGame()
    myGame.eventLoop()