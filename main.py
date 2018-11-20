'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart

Credits:
framework created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15

Description: This is the main framework that joins other files and
allows them to interact to make a game

'''

import pygame
import player
import projectile
import enemies
import map
import math
import random

class PygameGame(object):

    def init(self):
        self.playerGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.entitiesGroup = pygame.sprite.Group()
        self.obstaclesGroup = pygame.sprite.Group()
        self.player1 = player.Player(self.width//8, self.height//2)
        self.player1.preDraw()
        self.playerGroup.add(self.player1)
        self.startBoard = map.startBoard
        print(self.startBoard)
        self.angle = 0
        self.timer = 0

        print(self.width,self.height)

    def mousePressed(self, x, y):
        if self.player1.rect != None:
            centerX = self.player1.x
            centerY = self.player1.y
            xDiff = x - (centerX)
            yDiff = y - (centerY)
            if xDiff == 0 and y < centerY:
                self.angle = math.pi/2
            elif xDiff == 0 and y > centerY:
                self.angle = 3*math.pi/2
            elif yDiff == 0 and x > centerX:
                self.angle = 0
            elif yDiff == 0 and x < centerX:
                self.angle = math.pi
            else:
                self.angle = math.pi/2 + math.atan(xDiff/-yDiff)
                if y > centerY:
                    self.angle *= -1
                else:
                    self.angle = math.pi - self.angle


            bullet = projectile.Projectile(centerX,centerY,self.angle)
            self.bulletGroup.add(bullet)


    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass
    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        if keyCode == 119: # W
            self.player1.isRight = False
            self.player1.isLookRight, self.player1.isLookLeft = True, False
        if keyCode == 97: # A
            self.player1.isLeft = False
            self.player1.isLookRight, self.player1.isLookLeft = False, True
        if keyCode == 115: # S
            self.player1.isLeft = False
            self.player1.isLookRight, self.player1.isLookLeft = False, True
        if keyCode == 100: # D
            self.player1.isRight = False
            self.player1.isLookRight, self.player1.isLookLeft = True, False

    def timerFired(self, dt):
        self.timer += 1
        keyCode = pygame.key.get_pressed()
        if keyCode[119]:  # W
            if (self.player1.isLeft, self.player1.isRight) == (False, False):
                self.player1.isRight = True
            self.player1.velocity[1] = -self.player1.speed
            self.player1.velocity[0] = 0
            self.playerGroup.update()

        if keyCode[97]:  # A
            self.player1.isLeft, self.player1.isLookLeft = True, True
            self.player1.velocity[0] = -self.player1.speed
            self.player1.velocity[1] = 0
            self.playerGroup.update()

        if keyCode[115]:  # S
            if (self.player1.isLeft, self.player1.isRight) == (False, False):
                self.player1.isLeft = True
            self.player1.velocity[1] = self.player1.speed
            self.player1.velocity[0] = 0
            self.playerGroup.update()
        if keyCode[100]:  # D
            self.player1.isRight, self.player1.isLookRight = True, True
            self.player1.velocity[0] = self.player1.speed
            self.player1.velocity[1] = 0
            self.playerGroup.update()


        self.bulletGroup.update()

        if self.timer % 200 == 0:
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            enemy = enemies.Enemy(x,y)
            self.entitiesGroup.add(enemy)





    def redrawAll(self, screen):

        for i in range(len(self.startBoard)):
            for j in range(len(self.startBoard)):
                width = self.width//len(self.startBoard)
                height = self.height//len(self.startBoard)
                x = j * (width)
                y = i * (height)
                if self.startBoard[i][j] != 0:
                    pygame.draw.rect(screen,(255,255,0),(x,y,width,height))



        self.player1.preDraw()
        pygame.sprite.Group.draw(self.playerGroup,screen)

        # returns hit enemy and deletes the bullet and enemy from the game
        if (pygame.sprite.groupcollide(self.bulletGroup,self.entitiesGroup,True,True)):
            print("yeaaaahhhaa")

        pygame.sprite.Group.draw(self.bulletGroup, screen)

        pygame.sprite.Group.draw(self.entitiesGroup, screen)




    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=800, height=600, fps=50, title="John's TP"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                    self.redrawAll(screen)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()


