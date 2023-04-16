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

logo_surface = pygame.image.load('assets/logo.png')
player_x = 300
player_y = 300

# assets
background = pygame.image.load('assets/Background.png')
ground = pygame.image.load('assets/Ground.png')

# player
class Player():
    def __init__(self, x, y):
        logo_surface = pygame.image.load('assets/logo.png')
        self.image = pygame.transform.scale(logo_surface, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        dx = 0
        dy = 0

        #get keypresses 
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        
        #check for collisions (later)

        #update player coordinates (also later)
        self.rect.x += dx
        self.rect.x += dy

        #draw player onto screen
        screen.blit(self.image, self.rect)



player = Player(200,300)




# ----------------- GAME LOOP -----------------
while True:

    # PLAYER INPUT

    # --- old version (working) ---
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_a]:
    #    player_x -= 2
    #if keys[pygame.K_d]:
    #    player_x += 2

    # --- new version ---
    #key = pygame.key.get_pressed()
    #if key[pygame.K_LEFT]:
    #    self.rect.x -= 5



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
    




