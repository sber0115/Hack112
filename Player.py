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
        self.center = [x, y]
        self.angle = 0
        self.lookingAt = [0, 0]
        self.velocity = [0, 0]
        self.speed = 5
        self.color = (0, 0,0)
        self.gunLength = 50

    def updateRect(self):
        # print('a', self.rect.x)
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
        self.color = (255,0,0)
        self.position = [x, y]
        # self.rect = (self.position[0] - self.radius, self.position[1] - self.radius,
        #         self.position[0] + self.radius, self.position[1] + self.radius)

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.center[0], self.center[1]), self.radius)

    def updateRect(self, display):
        self.rect = pygame.draw.circle(display, self.color, (self.center[0], self.center[1]), self.radius)
        
    def update(self):

        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

    def chase(self, prey):
        xDistance = self.position[0] - prey.center[0]
        yDistance = self.position[1] - prey.center[1]

        if yDistance < 0:
            self.velocity[1] = 1*abs(prey.velocity[1])*2 + 1
        else:
            self.velocity[1] = -1*abs(prey.velocity[1])*2 - 1

        if xDistance < 0:
            self.velocity[0] = 1*abs(prey.velocity[0])*2 + 1
        else:
            self.velocity[0] = -1*abs(prey.velocity[0])*2 - 1