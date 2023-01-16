
# MAIN ITEMS
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
testFont = pygame.font.Font('font/Pixeltype.ttf', 50)

# SKY GROUND & TEXT SURFACES
skySurface = pygame.image.load('graphics/Sky.png').convert()
groundSurface = pygame.image.load('graphics/ground.png').convert()
textSurface = testFont.render('My game', False, 'Black')

# SNAIL
snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snailXPos = 600
snailRectangle = snailSurface.get_rect(midbottom = (snailXPos,300))

# PLAYER
playerSurface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
playerRectangle = playerSurface.get_rect(midbottom = (80,300))

# MASTER WHILE LOOP
while True:

    # GAME CLOSER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # SKY GROUND & TEXT RENDERER
    screen.blit(skySurface, (0,0))
    screen.blit(groundSurface, (0,300))
    screen.blit(textSurface, (300,50))

    # SNAIL MOVEMENT
    snailRectangle.left -= 4
    if snailXPos < -100: snailXPos = 800

    # SNAIL & PLAYER RENDERER
    screen.blit(snailSurface, snailRectangle)
    screen.blit(playerSurface, playerRectangle)

    # RUNTIME FUNCTIONS
    pygame.display.update()
    clock.tick(60) 
