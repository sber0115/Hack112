import pygame
import math

class Players(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()

        self.position = [x - self.rect.width//2, y - self.rect.height//2]
        self.center = [x, y]
        self.angle = 0
        self.lookingAt = [0,0]
        self.velocity = [0,0]
        self.speed = 5
        self.color = (0, 0,0)
        self.gunLength = 50


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



# class Enemy(Player):
#     def __init__():
