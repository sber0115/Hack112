import module_manager
module_manager.review()
import pygame


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
        self.entities = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()


        self.enemy = Player.Enemy("", self.width - 20, self.height - 20)
        self.mike = Player.Players("kimchee.jpg", self.width//2, self.height//2)
        self.entities.add(self.mike)
        self.entities.add(self.enemy)
        # print(len(self.entities))
        
    def mousePressed(self, x, y):
        self.mike.color = (255,0,0)
        mikesPosition = self.mike.position
        bulletToAdd = Bullets.Bullet(mikesPosition[0], mikesPosition[1])
        self.bullets.add(bulletToAdd)

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

    def timerFired(self, dt):
        self.enemy.chase(self.mike)
        if self.isKeyPressed(119):
            self.mike.velocity[1] = -self.mike.speed
        elif self.isKeyPressed(115):
            self.mike.velocity[1] = self.mike.speed
        else: self.mike.velocity[1] = 0
        
        
        if self.isKeyPressed(97):
            self.mike.velocity[0] = -self.mike.speed
        elif self.isKeyPressed(100):
             self.mike.velocity[0] = self.mike.speed
        else: self.mike.velocity[0] = 0
        
        
        # print()
        self.mike.update()
        self.enemy.update()
        
    def redrawAll(self, screen):

        self.mike.draw(screen)
        self.enemy.draw(screen)

    
    def isKeyPressed(self, key):
            
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=60, title="112 Pygame Game"):
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
