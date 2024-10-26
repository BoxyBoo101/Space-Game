import pygame
import random
import time
import pygame

pygame.init()
clock = pygame.time.Clock()
SCREENWIDTH = 1200
SCREENHEIGHT = 900
display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Space")
IsRocket = False
launchsound = pygame.mixer.Sound("Assets/launch.mp3")
boom = pygame.mixer.Sound("Assets/boom.mp3")
backround = pygame.mixer.Sound("Assets/backround.mp3")
launchsound.set_volume(0.2)
boom.set_volume(0.4)
inf = 999999999

musicchannel = pygame.mixer.find_channel()
musicchannel.play(backround, inf)
spaceshipimg = pygame.image.load("Assets/spaceship.png")
spaceshipimg = pygame.transform.scale(spaceshipimg, (100, 100))
spaceshipimg = pygame.transform.rotate(spaceshipimg, -90)

rocketimg = pygame.image.load("Assets/rocket.png")
rocketimg = pygame.transform.scale(rocketimg, (100, 100))

alienimg = pygame.image.load("Assets/alien.png")
alienimg = pygame.transform.scale(alienimg, (100, 41))
aliens = []

background = pygame.image.load("Assets/backgrounds/stars.png")
background = pygame.transform.scale(background, (SCREENWIDTH, SCREENHEIGHT))
backroundx = 0

gameoverimg = pygame.image.load("Assets/gameover.png")
gameoverimg = pygame.transform.scale(gameoverimg, (SCREENWIDTH, SCREENHEIGHT))
oversound = pygame.mixer.Sound("Assets/gameover.mp3")

class Alien:
    def __init__(self):
        self.rect = alienimg.get_rect(x = SCREENWIDTH, y = random.randint(0, SCREENHEIGHT - 100))
        self.speed = random.randint(4, 7)
    def move(self):
        self.rect.x -= self.speed

class Spaceship:
    def __init__(self):
        self.image = spaceshipimg
        self.rect = spaceshipimg.get_rect(center = (75, SCREENHEIGHT / 2))
    def move(self, directionY):
        self.rect.y += directionY
        self.rect.y = max(0, min(SCREENHEIGHT - self.rect.height, self.rect.y))
            
class Rocket:
    def __init__(self):
        self.image = rocketimg
        self.rect = rocketimg.get_rect(x = 75, y = 0)
    def rocketfire(self):
        self.rect.x += 20

def gameover():
    pygame.mixer.Channel.pause(musicchannel)
    offset = 900
    time.sleep(1)
    oversound.play()
    time.sleep(0.1)
    for i in range(150):
        offset -= 6
        display.blit(gameoverimg, (0, offset))
        pygame.display.update()
        clock.tick(60)
    time.sleep(4)
    run = False
    quit()
spaceship = Spaceship()
rocket = Rocket()

pygame.time.set_timer(pygame.USEREVENT, 2000)
run = True
while run:
    for event in   pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.USEREVENT:
            aliens.append(Alien())

    keys = pygame.key.get_pressed()
    if keys [pygame.K_w]:
        spaceship.move(-10)
    elif keys [pygame.K_s]:
        spaceship.move(10)
    elif pygame.mouse.get_pressed()[0]:
        if IsRocket != True:
            launchsound.play()
            IsRocket = True

    for alien in aliens[:]:
        alien.move()
        if alien.rect.right < 0:
            aliens.remove(alien)
            pygame.mixer.Channel.pause(musicchannel)
            offset = 900
            time.sleep(1)
            oversound.play()
            time.sleep(0.1)
            for i in range(150):
                offset -= 6
                display.blit(gameoverimg, (0, offset))
                pygame.display.update()
                clock.tick(60)
            time.sleep(4)
            run = False

#       if alien.rect.colliderect(spaceship.rect):
#            aliens.remove(aliessssn)
#            boom.play()

        if alien.rect.colliderect(rocket.rect):
            if IsRocket != False:
                aliens.remove(alien)
                boom.play()

    if IsRocket == True:
        rocket.rocketfire()
        if rocket.rect.x > 1400:
            IsRocket = False
    else:
        rocket.rect.x, rocket.rect.y = spaceship.rect.x, spaceship.rect.y
    backroundx += 2
    if backroundx > 1200:
        backroundx = 0

    display.blit(background, (backroundx * -1, 0))
    display.blit(background, (backroundx * -1 + 1200, 0))

    display.blit(rocket.image, rocket.rect)
    display.blit(spaceship.image, spaceship.rect)
    for alien in aliens:
        display.blit(alienimg, alien.rect)

    pygame.display.flip()
    clock.tick(60)
pygame.display.flip
pygame.quit()


