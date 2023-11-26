import pygame
from pygame import mixer
from pygame.locals import *
from pygame.key import ScancodeWrapper
import sys
import copy

# constant variables
SCREEN_SIZE = (1080, 720)
FLOOR_HEIGHT = 635
SPAWN_POS_X = 400
SPAWN_POS_Y = 10
JUMP_VEL = -80
SIDE_VEL = 20

# init
mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Snowball: A Sandbox Game")
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
        self.radius = self.rect.height / 2
        self.vel_y = 0
        self.vel_x = 0
        self.stop = False
        self.angle = 0

    def is_not_jumping(self):
        return self.rect.bottom >= FLOOR_HEIGHT

    def grow_snowball(self):
        if self.is_not_jumping():
            self.rect.width += 1
            self.rect.height += 1
            self.radius = self.rect.height / 2
            self.image = pygame.transform.scale(
                (snowball_img), (self.rect.width, self.rect.height)
            )

    def handle_upppkey(self, key: ScancodeWrapper):
        if key[pygame.K_UP] and (self.stop or self.is_not_jumping()):
            jump_fx.play()
            self.vel_y = JUMP_VEL
            self.stop = False

    def handle_R(self, key: ScancodeWrapper):
        if key[pygame.K_r]:
            parked_players.clear()

    def handle_sidekey(self, key: ScancodeWrapper, which_key: int, dir: int):
        if key[which_key]:
            self.vel_x = dir * SIDE_VEL
            self.grow_snowball()
            self.angle = (self.angle + 90) % 360

    def handle_downkey(self, key: ScancodeWrapper):
        if key[pygame.K_DOWN] and (self.is_not_jumping() or self.stop):
            old_self = self.reset_self()
            parked_players.append(old_self)

    def reset_self(self):
        old_self = copy.copy(self)
        new_self = Player(SPAWN_POS_X, SPAWN_POS_Y, snowball_img)
        self.__dict__ = new_self.__dict__  #https://stackoverflow.com/a/7940581
        print(new_self.__dict__)
        return old_self

    def handle_gravity(self):
        self.vel_y += 10
        if self.vel_y > 10:
            self.vel_y = 10
        self.rect.y += self.vel_y

    def handle_friction(self):
        if self.vel_x > 0:
            self.vel_x -= 1
        elif self.vel_x < 0:
            self.vel_x += 1

        if self.vel_x > 10:
            self.vel_x = -10
        elif self.vel_x < -10:
            self.vel_x = 10

        self.rect.x += self.vel_x

    #If player is below floor, move it back up
    def handle_floor(self):
        if self.rect.bottom > FLOOR_HEIGHT:
            self.rect.bottom = FLOOR_HEIGHT

    def handle_collisions(self):
        for p in parked_players:
            if pygame.sprite.collide_circle(self, p): #uses radius for collision detection
                print("collision")
                self.stop = True

    def update(self):
        key = pygame.key.get_pressed()

        # Check restart key
        self.handle_R(key)

        if not self.stop:
            # handle keypresses
            self.handle_sidekey(key, pygame.K_LEFT, 1)
            self.handle_sidekey(key, pygame.K_RIGHT, -1)

            # handle physics
            self.handle_gravity()
            self.handle_friction()
            self.handle_floor()
            self.handle_collisions()
        
        self.handle_upppkey(key)
        self.handle_downkey(key)

        # if key[pygame.K_UP] and self.is_not_jumping():
        #     pass

    def blit(self):
        # draw player onto screen
        a = pygame.transform.rotate(self.image, self.angle)
        screen.blit(a, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


clock.tick(60)
player = Player(SPAWN_POS_X, SPAWN_POS_Y, snowball_img)
parked_players = []

# ----------------- GAME LOOP -----------------
while True:
    # UPDATE
    pygame.display.update()
    player.update()

    # DRAW
    screen.blit(background, (0, 0))
    screen.blit(ground, (0, 630))
    player.blit()
    for p in parked_players:
        p.blit()

    # QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# ----------------- GAME LOOP END -----------------
