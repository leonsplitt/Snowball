import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Leon's Game")
clock = pygame.time.Clock()

#plaintest_surface = pygame.Surface((800,600))
#plaintest_surface.fill('Red')
logo_surface = pygame.image.load('assets/logo.png')
logo_x_pos = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    logo_x_pos += 4
    if logo_x_pos < 100: logo_x_pos = 600
    if logo_x_pos > 700: logo_x_pos = 100
    #screen.blit(plaintest_surface,(0,0))
    screen.blit(logo_surface,(logo_x_pos,200))
    # somehow moves weierdly right now
    

    pygame.display.update()
    clock.tick(60)





