import pygame
from sys import exit

# constant variables
SCREEN_SIZE = (1080, 720)

# init
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Snowball")
# clock = pygame.time.Clock()
# clock.tick(60)

BLUE = (0, 0, 255)


dx = 200
dy = 150

while True:
    pygame.display.update()

    # DRAW
    # screen.blit(background, (0,0))

    background = pygame.draw.rect(screen, BLUE, pygame.Rect(dx, dy, 100, 50))

    # get keypresses
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        dx -= 1
    if key[pygame.K_RIGHT]:
        dx += 1
    if key[pygame.K_UP]:
        dy -= 1
    if key[pygame.K_DOWN]:
        dy += 1

    allblue = True

    for i in range(1080):
        aww = screen.get_at((i, 0))

        if aww != BLUE:
            allblue = False
            break

    if allblue == True:
        print("izz blu")
    else:
        print("iwas anderes")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
