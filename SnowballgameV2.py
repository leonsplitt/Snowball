import pygame
from sys import exit

# constant variables
SCREEN_SIZE = (1080, 720)

# init
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Snowball")
clock = pygame.time.Clock()
clock.tick(60)

BLUE = (0, 0, 255)


dx = 200
dy = 150

while True:
    pygame.display.update()

    # draw the player on the screen
    player = pygame.draw.rect(screen, BLUE, pygame.Rect(dx, dy, 100, 50))

    # handle movements with arrow keys
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        dx -= 1
    if key[pygame.K_RIGHT]:
        dx += 1
    if key[pygame.K_UP]:
        dy -= 1
    if key[pygame.K_DOWN]:
        dy += 1

    # check the whole screen is blue
    allblue = True
    for j in range(SCREEN_SIZE[1]):
        for i in range(SCREEN_SIZE[0]):
            aww = screen.get_at((i, j))
            if aww != BLUE:
                allblue = False
                break

    if allblue == True:
        print("izz blu")
    else:
        print("iwas anderes")

    # exit if closing window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
