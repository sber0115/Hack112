import module_manager
module_manager.review()
import pygame
import Boardmaker
import Box
import Player

'''
pygamegame.py
created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15
use this code in your term project if you want
- CITE IT
- you can modify it to your liking
  - BUT STILL CITE IT
- you should remove the print calls from any function you aren't using
- you might want to move the pygame.display.flip() to your redrawAll function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''

class PygameGame(object):
    def init(self):
        
        self.board = Boardmaker.makeBoard(20,Boardmaker.obstacles)
        self.sizex = self.width // 10
        self.sizey = self.height // 10
        self.scrollx = 0
        self.scrolly = 0
        self.xOffset = 0
        self.yOffset = 0
        
        self.entities = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.clock = 0

        self.enemy = Player.Enemy("", self.width - 20, self.height - 20)
        self.mike = Player.Players("kimchee.jpg", self.width//2, self.height//2)
        self.entities.add(self.mike)

        self.entities.add(self.enemy)
        print(self.entities)
        self.display = None
        # print(len(self.entities))
        
    def mousePressed(self, x, y):
        self.mike.color = (255,0,0)

    def mouseReleased(self, x, y):
        self.mike.color = (0,0,0)

    def mouseMotion(self, x, y):
        self.mike.lookingAt = [x,y]
        self.mike.look(x, y)

    def mouseDrag(self, x, y):
        self.mike.lookingAt = [x,y]
        self.mike.look(x, y)

    def keyPressed(self, keyCode, modifier):
        pass
            
    def keyReleased(self, keyCode, modifier):
        pass

    def moveMap(self):

        if self.isKeyPressed(119):

            self.scrolly = self.mike.speed
            self.enemy.center[1] += 5
            
        elif self.isKeyPressed(115):
            self.scrolly = -self.mike.speed
            self.enemy.center[1] -= 5
        else:
            self.scrolly = 0

        if self.isKeyPressed(97):
            self.scrollx = self.mike.speed
            self.enemy.center[0] += 5
            
        elif self.isKeyPressed(100):
            self.scrollx = -self.mike.speed
            self.enemy.center[0] -= 5
            
        else:
            self.scrollx = 0
            self.enemy.velocity[0] = 0
            
        
        
    def timerFired(self, dt):
        self.clock += 1
        self.moveMap()
        self.xOffset += self.scrollx
        self.yOffset += self.scrolly

        # if self.clock % 4 == 0:
       
        self.enemy.update()
        
        # self.enemy.chase(self.mike)


        if self.display != None:
            # print('enemy', self.enemy.rect)
            # print('mike', self.mike.rect)
            self.enemy.updateRect(self.display)
            # pygame.sprite.spritecollide(self.mike, self.entities, True)
           
            collided = pygame.sprite.spritecollide(self.mike, self.entities, False)
            # print(self.entities)
            
        # groupcollide(group1, group2, dokill1, dokill2, collided=None)

        
    def redrawAll(self, screen):
        for i in range(20):
            for j in range(20):
                X = j* self.sizex + self.xOffset
                Y = i * self.sizey + self.yOffset
                if self.board[i][j] == 1:
                    obs = Box.Box(X,Y,self.sizex,self.sizey)
                    Box.Box.draw(obs,screen)
                    

        
        self.display = screen
        self.enemy.updateRect(screen)
        
        for sprite in self.entities:
            sprite.draw(screen)

        


        # self.mike.draw(screen)
        # self.enemy.draw(screen)
    
    def isKeyPressed(self, key):
            
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=600, fps=60, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
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