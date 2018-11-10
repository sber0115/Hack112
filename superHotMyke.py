import module_manager
module_manager.review()
import pygame

#### Classes ####

'''class Bullet(object):
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


'''
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

def startKeyPressed(event, data):
    if event.keysym == "space":
        data.scrollY = 0

def startTimerFired(data):
    if data.scrollY >= 0:
        data.scrollY -= 25

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

def gameMousePressed(event, data):
    pass
    
def gameKeyPressed(event, data):
    pass

def gameTimerFired(data):
    pass

def gameRedrawAll(canvas, data):
    canvas.create_rectangle(-1, -1, data.width, data.height, fill = "red")


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
    elif data.mode == "gameState":
        gameMousePressed(event, data)
    elif data.mode == "gameOverState":
        gameOverMousePressed(event, data)

def keyPressed(event, data):
    if data.mode == "startState":
        startKeyPressed(event, data)
    elif data.mode == "gameState":
        gameKeyPressed(event, data)
    elif data.mode == "gameOverState":
        gameOverKeyPressed(event, data)

def timerFired(data):
    if data.mode == "startState":
        startTimerFired(data)
    elif data.mode == "gameState":
        gameTimerFired(data)
    elif data.mode == "gameOverState":
        gameOverTimerFired(data)

def redrawAll(canvas, data):
    if data.mode == "startState":
        startRedrawAll(canvas, data)
    elif data.mode == "instructionState":
        instructionRedrawAll(canvas, data)
    elif data.mode == "gameState":
        gameRedrawAll(canvas, data)
    elif data.mode == "gameOverState":
        gameOverRedrawAll(canvas, data)

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
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)