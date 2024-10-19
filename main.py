import pygame
import random
pygame.init()
clock = pygame.time.Clock()
SCREENWIDTH = 1200
SCREENHEIGHT = 900
display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

SpaceShip = pygame.image.load("Assets/spaceship.png")
SpaceShip = pygame.transform.scale(SpaceShip, (100, 100))
SpaceShip = pygame.transform.rotate(SpaceShip, -90)
ShipX, ShipY = 40, 300

rocket = pygame.image.load("Assets/rocket.png")
rocket = pygame.transform.scale(rocket, (100, 100))
rocketx, rockety = 40, 300

alienimg = pygame.image.load("Assets/alien.png")
alienimg = pygame.transform.scale(alienimg, (100, 100))
alienx, alieny = 800, random.randint(0, 900)
aliens = []

background = pygame.image.load("Assets/backgrounds/bliss.jpeg")
background = pygame.transform.scale(background, (SCREENWIDTH, SCREENHEIGHT))

class Alien:
    def __init__(self):
        self.rect = alienimg.get_rect(x = SCREENWIDTH, y = random.randint(0, SCREENHEIGHT - 100))
    def move(self):
        self.rect.x -= 3
            
        print("x " + str(self.rect.x))
        print("y " + str(self.rect.y))

pygame.time.set_timer(pygame.USEREVENT, 3000)
run = True
while run:
    for event in   pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
        elif event.type == pygame.USEREVENT:
            aliens.append(Alien())
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        if ShipY > 0:
            ShipY -= 10
    elif keys [pygame.K_DOWN]:
        if ShipY < SCREENHEIGHT - 100:    
            ShipY += 10
    
    for alien in aliens[:]:
        alien.move()
    for alien in aliens:
        display.blit(alienimg, (alienx, alieny))

    display.blit(background, (0, 0))
    display.blit(SpaceShip, (ShipX, ShipY))

    pygame.display.flip()
    clock.tick(5)
pygame.display.flip
pygame.quit()


