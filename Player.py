import pygame
import math

class Players(pygame.sprite.Sprite):
    def __init__(self, image, weaponImage):
        pygame.sprite.Sprite.__init__(self)

        self.position = [20 ,20]
        self.angle = 0
        self.lookingAt = [0,0]
        self.velocity = [0,0]
        self.speed = 5
        self.color = (255, 0,0)
        
   
     
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        
        self.weapon = pygame.image.load(weaponImage).convert_alpha()

        self.baseImage = self.image.copy()

    def update(self):
        # print(self.width)
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    # def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        # w, h = self.image.get_size()
        # self.width, self.height = w, h
        # self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def look(self, mouseX, mouseY):
        print('a')
        xDif = abs(mouseX - self.position[0])
        yDif = abs(mouseY - self.position[1])
        self.angle = math.atan(yDif/xDif)

        self.lookingAt = [mouseX, mouseY]
    
    def draw(self, display):
        pygame.draw.line(display, self.color , (self.position[0], self.position[1]), (self.lookingAt[0], self.lookingAt[1]), 4 )
        display.blit(self.image, self.position)
        # pygame.surface.Surface.blit(self.weapon, screen)


# class Enemy(Player):
#     def __init__():
