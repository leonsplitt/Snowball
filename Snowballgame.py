import pygame
from pygame.locals import *
from sys import exit

# constant variables
SCREEN_SIZE = (1280,720)

# init
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Leon's Game")
clock = pygame.time.Clock()

# assets
background = pygame.image.load('assets/Background.png')
ground = pygame.image.load('assets/Ground.png')

# player
class Player():
    def __init__(self, x, y):
        logo_surface = pygame.image.load('assets/logo.png')
        self.image = pygame.transform.scale(logo_surface, (player_x,player_y))


# logo_surface = pygame.image.load('assets/logo.png')
player_x = 300
player_y = 300


# game loop
while True:
    # INPUT

    # player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= 2
    if keys[pygame.K_d]:
        player_x += 2

    # update
    pygame.display.update()
    clock.tick(60)

    #draw
    screen.blit(background, (0,0))
    screen.blit(ground, (0,630))
    screen.blit(logo_surface,(player_x,player_y))





    #quit & frame things
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    




