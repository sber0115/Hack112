import pygame
import random


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, sizex, sizey):
        super(Box, self).__init__()
        self.x, self.y = x, y
        self.sizex, self.sizey = sizex, sizey
        self.rect = pygame.Rect(x, y, sizex, sizey)
        (self.r, self.g, self.b) = 255, 0, 0
        # self.image = pygame.Surface((size,size),pygame.SRCA)
        # self.image = self.image.convert_alpha()

    def draw(self, surface):
        pygame.draw.rect(surface, (self.r, self.g, self.b), self.rect)