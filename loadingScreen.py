import module_manager
module_manager.review()
import pygame


#### Classes ####

class Bullet(object):
    # Model
    def __init__(self, cx, cy, angle, speed):
        # A bullet has a position, a size, a direction, and a speed
        self.cx = cx
        self.cy = cy
        self.r = 5
        self.angle = angle
        self.speed = speed
    
    # View
    def draw(self, canvas):
        canvas.create_oval(self.cx - self.r, self.cy - self.r, 
                           self.cx + self.r, self.cy + self.r,
                           fill="white", outline=None)

    # Controller
    def moveBullet(self):
        # Move according to the original trajectory
        self.cx += math.cos(math.radians(self.angle))*self.speed
        self.cy -= math.sin(math.radians(self.angle))*self.speed

    def collidesWithWall(self, width, height):
        # Check if the bullet and the wall or overlaps it at all
        return self.cx - self.r <= 0 or self.cx + self.r >= width or \
            self.cy - self.r <= 0 or self.cy + self.r >= height
            
    def collidesWithObject(self, other):
        # Check if the bullet and an object overlap at all
        dist = ((other.cx - self.cx)**2 + (other.cy - self.cy)**2)**0.5
        return dist < self.r + other.r
    
    def isOffscreen(self, width, height):
        # Check if the bullet has moved fully offscreen
        return (self.cx + self.r <= 0 or self.cx - self.r >= width) or \
               (self.cy + self.r <= 0 or self.cy - self.r >= height)

####Player and Enemy Classes


import pygame
import math

class Players(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)

        if image != "":
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
    
    def makeBullet(self):
        # Generates a bullet heading in the direction the ship is facing
        offset = 35
        x = self.position[0] + offset*math.cos(math.radians(self.angle)) 
        y = self.position[1] - offset*math.sin(math.radians(self.angle))
        
        return Bullet(x, y, self.angle, 20)
        
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
    

class Enemy(Players):
    def __init__(self,image, x,y):
        super().__init__(image, x,y)
        self.radius = 15
        self.color = (255,0,0)
        self.position = [x, y]

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.center[0], self.center[1]), self.radius)

    def chase(self, prey):
        xDistance = self.position[0] - prey.center[0]
        yDistance = self.position[1] - prey.center[1]

        if yDistance < 0:
            self.velocity[1] = 1
        else:
            self.velocity[1] = -1

        if xDistance < 0:
            self.velocity[0] = 1
        else:
            self.velocity[0] = -1

#### Pygame framework

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
        #bulletToAdd = Players.makeBullet(self.mike)
        #print(bulletToAdd)
        #self.bullets.add(bulletToAdd)
        #print(self.bullets)

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

    
    
#### Graphics Functions ####

from tkinter import *

#start screen dispatcher

def startMousePressed(event, data):
    if data.width//2 - data.buttonWidth//2 <= event.x <= data.width//2 + data.buttonWidth//2 \
    and data.scrollY + 5*data.height//6 <= event.y <= data.scrollY + 5*data.height//6 + data.buttonHeight:
        data.mode = "instructionState"
    elif data.width//2 - data.buttonWidth//2 <= event.x <= data.width//2 + data.buttonWidth//2 \
    and data.scrollY + 3*data.height//4 <= event.y <= data.scrollY + 3*data.height//4 + data.buttonHeight:
        data.mode = "gameState"
        game = PygameGame()
        game.run()


def startKeyPressed(event, data):
    if event.keysym == "space":
        data.scrollY = 0

def startTimerFired(data):
    if data.scrollY >= 0:
        data.scrollY -= 25

def draw():
    pass

def startRedrawAll(canvas, data):
    
    canvas.create_rectangle(-1, -1, data.width, data.height, fill = "greenyellow")
    startText = '''
    In  a  universe  where axolotls control time,
    
    an evil  group of  villains are trying to take
    
    possession  of  all axolotls  to harvest their 
    
    powers to rule the world. However, there lives 
    
    one man, our hero, Mike Taylor, who made a vow 
    
    to protect the last axolotl, Kimchee, all from
    
    wrongdoers. You  will take on the role of Mike, 
    
    trying  your  best  to  protect  him from harm.'''
        
    #creates scrolling text
    canvas.create_text(data.width//2, data.scrollY, anchor = S, text = startText, font = "Arial 30 bold")
    
    #creates press space to skip text
    if data.scrollY > 550:
        canvas.create_text(data.width//2, 10, anchor = N, text = "Press space to skip", font = "Arial 11 bold")
    
    #creates title
    canvas.create_text(data.width//2, data.scrollY + data.height//3, text = "THE LAST", font = "Arial 150 bold")
    canvas.create_text(data.width//2, data.scrollY + data.height//2, text = "AXOLOTL", font = "Arial 150 bold")
    
    #creates play button
    canvas.create_rectangle(data.width//2 - data.buttonWidth//2, \
    data.scrollY + 3*data.height//4, data.width//2 + data.buttonWidth//2, \
    data.scrollY + 3*data.height//4 + data.buttonHeight, fill = "black")
    canvas.create_text(data.width//2, data.scrollY + 3*data.height//4 + data.buttonHeight//2, text = "Play", font = "Arial 15 bold", fill = "white")
    
    #creates instructions button
    canvas.create_rectangle(data.width//2 - data.buttonWidth//2, \
    data.scrollY + 5*data.height//6, data.width//2 + data.buttonWidth//2, \
    data.scrollY + 5*data.height//6 + data.buttonHeight, fill = "black")
    canvas.create_text(data.width//2, data.scrollY + 5*data.height//6 + data.buttonHeight//2, text = "Instructions", font = "Arial 15 bold", fill = "white")
    
#instruction dispatcher

def instructionMousePressed(event, data):
    if data.width//2 - data.buttonWidth//2 <= event.x <= data.width//2 + data.buttonWidth//2 and \
    3*data.height//4 <= event.y <= 3*data.height//4 + data.buttonHeight:
        data.mode = "gameState"
        game = PygameGame()
        game.run()
    
def instructionRedrawAll(canvas, data):
    #creates instructions
    canvas.create_rectangle(-1, -1, data.width, data.height, fill = "yellow")
    canvas.create_text(data.width//2, data.height//4, text = "How to Play:", font = "Arial 50 bold")
    
    #recreates play button
    canvas.create_rectangle(data.width//2 - data.buttonWidth//2, \
    3*data.height//4, data.width//2 + data.buttonWidth//2, \
    3*data.height//4 + data.buttonHeight, fill = "black")
    canvas.create_text(data.width//2, 3*data.height//4 + data.buttonHeight//2, text = "Play", font = "Arial 15 bold", fill = "white")
    
#game dispatcher


## mode dispatcher
##calls all the functions within each respective function

def init(data): #initializes variables
    data.mode = "startState"
    data.scrollY = data.height + 500
    data.buttonWidth = 200
    data.buttonHeight = 50

def mousePressed(event, data): 
    if data.mode == "startState":
        startMousePressed(event, data)
    elif data.mode == "instructionState":
        instructionMousePressed(event, data)

def keyPressed(event, data):
    if data.mode == "startState":
        startKeyPressed(event, data)

def timerFired(data):
    if data.mode == "startState":
        startTimerFired(data)

def redrawAll(canvas, data):
    if data.mode == "startState":
        startRedrawAll(canvas, data)
    elif data.mode == "instructionState":
        instructionRedrawAll(canvas, data)



#################################################################
# use the run function as-is
#################################################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    #exitButton = Button(root, text = "Play", command = root.destroy).pack()
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)
