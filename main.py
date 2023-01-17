
# MAIN ITEMS
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
testFont = pygame.font.Font('font/Pixeltype.ttf', 50)

# SKY & GROUND SURFACES
skySurface = pygame.image.load('graphics/Sky.png').convert()
groundSurface = pygame.image.load('graphics/ground.png').convert()

# SCORE
scoreSurface = testFont.render('SCORE', False, 'Black')
scoreRectangle = scoreSurface.get_rect(center = (400,50))

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
        
        # if event.type == pygame.MOUSEMOTION:
        #     if playerRectangle.collidepoint(event.pos): print('collision')

    # SKY GROUND & SCORE RENDERER
    screen.blit(skySurface, (0,0))
    screen.blit(groundSurface, (0,300))
    pygame.draw.rect(screen,'Pink',scoreRectangle)
    screen.blit(scoreSurface, scoreRectangle)

    # SNAIL MOVEMENT
    snailRectangle.x -= 4
    if snailRectangle.right < 0: snailRectangle.left = 800

    # SNAIL & PLAYER RENDERER
    screen.blit(snailSurface, snailRectangle)
    screen.blit(playerSurface, playerRectangle)

    # COLLISION DETETCION
    if playerRectangle.colliderect(snailRectangle):
        pass

    # mousePos = pygame.mouse.get_pos()
    # if playerRectangle.collidepoint(mousePos): print('collision')

    # RUNTIME FUNCTIONS
    pygame.display.update()
    clock.tick(60)
