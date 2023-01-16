import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
testFont = pygame.font.Font('font/Pixeltype.ttf', 50)

skySurface = pygame.image.load('graphics/Sky.png')
groundSurface = pygame.image.load('graphics/ground.png')
textSurface = testFont.render('My game', False, 'Black')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(skySurface, (0,0))
    screen.blit(groundSurface, (0,300))
    screen.blit(textSurface, (300,50))

    pygame.display.update()
    clock.tick(60) 
