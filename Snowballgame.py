import pygame
from pygame import mixer
from pygame.locals import *
from pygame.key import ScancodeWrapper
from sys import exit

# constant variables
SCREEN_SIZE = (1080, 720)
FLOOR_HEIGHT = 635
SPAWN_POS_X = 300
SPAWN_POS_Y = 300
JUMP_VEL = -80
SIDE_VEL = 20

# init
mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Leon's Game")
clock = pygame.time.Clock()


# load assets
background = pygame.image.load("assets/Background.png")
ground = pygame.image.load("assets/Ground.png")
snowball_img = pygame.image.load("assets/logo.png")

# load sounds
pygame.mixer.music.load("assets/night.mp3")
pygame.mixer.music.play(-1, 0.0, 0)
jump_fx = pygame.mixer.Sound("assets/jump2.mp3")
jump_fx.set_volume(0.1)


# player
class Player:
    def __init__(self, x, y, snowball_img):
        self.image = pygame.transform.scale((snowball_img), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.moved = False

    def is_not_jumping(self):
        return self.rect.bottom == FLOOR_HEIGHT

    def grow_snowball(self):
        self.rect.width += 1
        self.rect.height += 1
        self.image = pygame.transform.scale(
            (snowball_img), (self.rect.width, self.rect.height)
        )

    def handle_sidekey(self, key: ScancodeWrapper, which_key: int, dir: int):
        if key[which_key] and self.moved == False:
            self.vel_x = dir * SIDE_VEL
            self.moved = True
            self.grow_snowball()
        elif key[which_key] == False:
            self.moved = False

    def update(self):
        dx = 0
        dy = 0

        # handle keypresses
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.is_not_jumping():
            jump_fx.play()
            self.vel_y = JUMP_VEL

        self.handle_sidekey(key, pygame.K_LEFT, 1)
        self.handle_sidekey(key, pygame.K_RIGHT, -1)

        # add gravity
        self.vel_y += 10
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # add friction
        if self.vel_x > 0:
            self.vel_x -= 1
        elif self.vel_x < 0:
            self.vel_x += 1

        if self.vel_x > 10:
            self.vel_x = -10
        elif self.vel_x < -10:
            self.vel_x = 10

        dx += self.vel_x

        # TODO: check for collisions with other snowballs (later)

        # update player coordinates (also later)
        self.rect.x += dx
        self.rect.y += dy

        # if player is below floor, move it back up
        if self.rect.bottom > FLOOR_HEIGHT:
            self.rect.bottom = FLOOR_HEIGHT
            dy = 0

    def blit(self):
        # draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


# def freeze(current_player: Player, static_list):
#    static_list.append(current_player)
#    current_player = Player(SPAWN_POS_X,SPAWN_POS_Y, snowball_img)


# static_list = []
clock.tick(60)
player = Player(SPAWN_POS_X, SPAWN_POS_Y, snowball_img)


# ----------------- GAME LOOP -----------------
while True:
    # UPDATE
    pygame.display.update()

    # DRAW
    screen.blit(background, (0, 0))
    screen.blit(ground, (0, 630))
    # for i in static_list:
    #    i.blit()
    # screen.blit(logo_surface,(player_x,player_y))

    # the cool function that does everything:

    player.update()
    player.blit()
    # freeze with down key
    # key = pygame.key.get_pressed()
    # if key[pygame.K_DOWN]:
    #    freeze(player, static_list)

    # QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# ----------------- GAME LOOP END -----------------
