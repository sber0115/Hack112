'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: This code takes a given spritesheet and partitions it into individual character pictures. This allows
for animation of character movement.
'''

import pygame
pygame.init()


# takes given spritesheet and partitions it into usable subimages
def getFrames(surface, start, size, cols, rows):
    frames = []
    for i in range(rows):
        for j in range(cols):
            location = ((start[0]+size[0]*j+j+1),(start[1]+size[1]*i)+1)
            frames.append(surface.subsurface(pygame.Rect(location, size)))
    return frames
# reverses the given subimages
def getRevFrames(pics):
    frames = []
    for i in range(len(pics)):
        frames.append(pygame.transform.flip(pics[i],True,False))
    return frames




