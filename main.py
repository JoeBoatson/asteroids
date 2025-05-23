import pygame
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    game_loop = 5

    while game_loop > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    screen.fill(000000)
    pygame.display.flip()
if __name__ == "__main__":
    main()