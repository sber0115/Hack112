import pygame
import math

class Players(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)

        if image != "":
            self.image = pygame.image.load(image).convert()
            self.imageSize= self.image.get_rect()
            self.position = [x - self.imageSize.width//2, y - self.imageSize.height//2]
            self.rect = self.image.get_rect()
            self.rect.topleft = (x - self.imageSize.width//2, y - self.imageSize.height//2)
            self.rect.bottomright = (x + self.imageSize.width//2, y + self.imageSize.height//2)
        self.alive = True
        self.center = [x, y]
        self.angle = 0
        self.lookingAt = [0, 0]
        self.velocity = [0, 0]
        self.speed = 5
        self.color = (0, 0,0)
        self.gunLength = 50

    def updateRect(self):

        self.rect.topleft = self.position[0] - self.imageSize.width, self.position[1] - self.imageSize.height
        self.rect.bottomright = self.position[0] + self.imageSize.width, self.position[1] + self.imageSize.height

    def update(self):

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

    def look(self, mouseX, mouseY):

        xDif = mouseX - self.center[0]

        yDif = mouseY - self.center[1]

        if xDif == 0:
            self.angle = math.pi/2
        else:
            self.angle = math.atan(yDif/xDif)

        if xDif >= 0:
            newX = math.cos(self.angle) * self.gunLength + self.center[0]
            newY = math.sin(self.angle) * self.gunLength + self.center[1]

        elif xDif <= 0 :
            newX = -math.cos(self.angle) * self.gunLength + self.center[0]
            newY = -math.sin(self.angle) * self.gunLength + self.center[1]

        self.lookingAt = [newX, newY]
    
    def draw(self, display):
        pygame.draw.line(display, self.color, (self.center[0], self.center[1]), (self.lookingAt[0] , self.lookingAt[1]), 10 )
        display.blit(self.image, self.position)



class Enemy(Players):
    def __init__(self,image, x,y):
        super().__init__(image, x,y)
        self.radius = 15
        self.color = (0, 255,0)
        self.position = [x, y]

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.center[0], self.center[1]), self.radius)

    def updateRect(self, display):
        self.rect = pygame.draw.circle(display, self.color, (self.center[0], self.center[1]), self.radius)

    def chase(self, goalX, goalY, speedx, speedy):
        xDistance = self.center[0] - goalX
        yDistance = self.center[1] - goalY

        if yDistance < 0:
            self.velocity[1] = 1*abs(speedy)
        else:
            self.velocity[1] = -1*abs(speedy)

        if xDistance < 0:
            self.velocity[0] = 1*abs(speedx)
        else:
            self.velocity[0] = -1*abs(speedx )