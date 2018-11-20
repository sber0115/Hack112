'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: (line 30 of this file)
Image of Chef Kawaski character borrowed from Kirby Super Star and taken
from this website:
http://animegames.wikia.com/wiki/File:Chef_Kawasaki_(Kirby_Super_Star_-_Sprite_Sheets_-_Hitbox).png
Description: Defines the Player class containing all attributes of the player
'''



import pygame
import playerImages   #stores information for player images and animation

# sets player class with player attributes
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 4
        self.velocity = [0,0]
        self.isLookLeft = False
        self.isLeft = False
        self.isLookRight = True
        self.isRight = False
        self.walkCount = 0  # increments to determine player animation picture
        self.image ='testPics\chefK.png'
        self.getPics(self.image)


    def getPics(self,image):
        frameWidth = 55
        frameHeight = 65
        cols = 5
        rows = 1
        self.pics = playerImages.getFrames(pygame.image.load(image), (0, 0), (frameWidth, frameHeight), cols, rows)
        self.picsRev = playerImages.getRevFrames(self.pics)
        self.standingR = self.pics[0]
        self.standingL = self.picsRev[0]
        self.walkingR = [self.pics[1], self.pics[2], self.pics[3], self.pics[4]]
        self.walkingL = [self.picsRev[1], self.picsRev[2], self.picsRev[3], self.picsRev[4]]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]


    def preDraw(self):
        self.walkCount += 1
        if self.walkCount >= 20:
            self.walkCount = 0

        if self.isLeft:
            self.image = self.walkingL[self.walkCount // 5]
        elif self.isRight:
            self.image = self.walkingR[self.walkCount // 5]
        elif self.isLookLeft:
            self.image = self.standingL
        elif self.isLookRight:
            self.image = self.standingR
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)



