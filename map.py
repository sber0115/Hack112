import pygame
pygame.init()

def makeStartBoard(n):
    startBoard = []
    startBoard.append([0]*n)
    startBoard.append([0]+[2]*(n-5)+[0]*4)
    startBoard.append([0] + [2] + [1]*(n-7)+ [1] + [0]*4)
    for i in range(n-17):
        startBoard.append([0] + [2] + [0]*(n-7) + [2] + [0]*4)
    startBoard.append([0] + [2] + [0]*(n-7) + [2]*5)
    startBoard.append([0] + [2] + [0]*(n-7) + [1]*5)
    for i in range(4):
        startBoard.append([0] + [2] + [0]*(n-2))
    startBoard.append([0] + [2] + [0]*(n-7) + [2]*5)
    startBoard.append([0] + [2] + [0]*(n-7) + [2] + [1]*4)
    for i in range(n-17):
        startBoard.append([0] + [2] + [0]*(n-7) + [2] + [0]*4)
    startBoard.append([0] + [2]*(n-5) + [0]*5)
    startBoard.append([0] + [1]*(n-5) + [0]*4)
    return startBoard

startBoard = makeStartBoard(20)

print(startBoard)


