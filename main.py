import pygame
from sys import exit
pygame.init()

width = 800
height = 400

screen = pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all elements
    # update everything
    pygame.display.update()


