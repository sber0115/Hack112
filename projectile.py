'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: Defines the Projectiles class containing all attributes of the projectiles
'''

import pygame
import math
pygame.init()

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 10
        self.velocity = [self.speed*math.cos(angle),self.speed*-math.sin(angle)]
        self.image = pygame.image.load("testPics\omato.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update (self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]








