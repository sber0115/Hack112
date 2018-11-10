import pygame,time, os, math, random, copy

class Bullet(pygame.sprite.Sprite):
    def __init__(self, playerX, playerY):
        super(Bullet, self).__init__()
        self.x = playerX
        self.y = playerY
        self.velocities = [0,0]
        self.hasUpdated = False
        self.radius = 10
        self.rect = pygame.Rect(playerX - self.radius, playerY - self.radius,
                                2 * self.radius, 2 * self.radius)
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                    pygame.SRCALPHA)  # make it transparent
        self.image = self.image.convert_alpha()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.circle(self.image, (r, g, b),
                           (self.radius, self.radius), self.radius)

    def getRect(self):  # GET REKT
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                2 * self.radius, 2 * self.radius)

    def update(self, playerAngle):
        if not self.hasUpdated:
            print(playerAngle)
            self.hasUpdated = not self.hasUpdated
            print("velocities changed")
            self.velocities = [math.cos(playerAngle), math.sin(playerAngle)]
            print(self.velocities)
        else:
            self.x += self.velocities[0]
            self.y -= self.velocities[1]

        self.getRect()

    def removeBullets(self, other):
        if pygame.sprite.collide(self, other):
            return True
        return False



