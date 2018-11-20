#import module_manager
# module_manager.review()
import pygame
pygame.init()
winWidth = 500
winHeight = 500
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Test')




x = 0
y = 0
width = 40
height = 60
vel = 1
isJump = False
isLeft = False
isRight = False
jumpCount = 50

def redrawAll():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 0), (x, y, width, height))
    pygame.display.update()



run = True
while(run):
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        isLeft = True
        isRight = False
        x -= vel
        if x < 0:
            x += vel
    if keys[pygame.K_RIGHT]:
        isLeft = False
        isRight = True
        x += vel
        if x + width > winWidth:
            x -= vel

    if not isJump:
        if keys[pygame.K_UP]:
            y -= vel
            if y < 0:
                y += vel
        if keys[pygame.K_DOWN]:
            y += vel
            if y + height> winHeight:
                y -= vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -50:
            num = 2
            if jumpCount < 0:
                num = -2
            y -= num*((jumpCount/45)**2)
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 50

    redrawAll()




pygame.quit()
