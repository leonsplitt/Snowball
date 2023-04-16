import pygame
from pygame import mixer
import random
import time
import sys
from pygame.locals import *
from sys import exit

# constant variables
SCREEN_SIZE = (1280,720)

# init
pygame.mixer.pre_init(44100, -16,2, 512)
mixer.init()
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Leon's Game")
clock = pygame.time.Clock()

#logo_surface = pygame.image.load('assets/logo.png')
player_x = 300
player_y = 300

# load assets
background = pygame.image.load('assets/Background.png')
ground = pygame.image.load('assets/Ground.png')

# load sounds
pygame.mixer.music.load('assets/night.mp3')
pygame.mixer.music.play(-1, 0.0, 0)
jump_fx = pygame.mixer.Sound('assets/jump2.mp3')
jump_fx.set_volume(0.1)

# player
class Player():
    def __init__(self, x, y):
        logo_surface = pygame.image.load('assets/logo.png')
        self.image = pygame.transform.scale(logo_surface, (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0

        #get keypresses 
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
            jump_fx.play()
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_UP] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        
        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check for collisions (later)

        #update player coordinates (also later)
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > 635:
            self.rect.bottom = 635
            dy = 0

        #draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


player = Player(300,300)




# ----------------- GAME LOOP -----------------
while True:

    # PLAYER INPUT

    # --- old version (working) ---
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_a]:
    #    player_x -= 2
    #if keys[pygame.K_d]:
    #    player_x += 2


    # UPDATE
    pygame.display.update()
    clock.tick(60)

    #DRAW
    screen.blit(background, (0,0))
    screen.blit(ground, (0,630))
    #screen.blit(logo_surface,(player_x,player_y))

    #the cool function that does everything:
    player.update()

    #QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# ----------------- GAME LOOP END -----------------
    




