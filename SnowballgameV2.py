import pygame
from sys import exit

# constant variables
SCREEN_SIZE = (1080,720)

# init
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Snowball")
# clock = pygame.time.Clock()
#clock.tick(60)


while True:
    
    pygame.display.update()

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         exit()


