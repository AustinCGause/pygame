import pygame
from sys import exit
pygame.init()

width = 800
height = 400

screen = pygame.display.set_mode((width,height)) # this sets the window size
pygame.display.set_caption('Runner') # this changes the title of the window
clock = pygame.time.Clock()

while True:

    # inside this while loop, we are going to be drawing all elements and updating everything

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    '''
    This event loop ensures that there is a way for pygame to close the window, and the sys exit() module
    is better than just breaking the while loop, because it closes all the code at once. 
    '''

    pygame.display.update()
    clock.tick(60) 
    # this 60 is telling pygame that the while loop should not go more than 60 times a second


