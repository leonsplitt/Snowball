import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Leon's Game")
clock = pygame.time.Clock()

background = pygame.image.load('assets/Background.png')
ground = pygame.image.load('assets/Ground.png')

box = pygame.Surface((50,50))
box.fill('Red')

#logo_surface = pygame.image.load('assets/logo.png')
#logo_x_pos = 200

screen.blit(background, (0,0))
screen.blit(box,(500,400))
screen.blit(ground, (0,630))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(logo_surface,(logo_x_pos,200))
    

    pygame.display.update()
    clock.tick(60)





