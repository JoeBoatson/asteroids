import pygame
from constants import *
from player import *
from circleshape import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("black") # fill screen with black
        player.draw(screen) # draw the player
        player.update(dt)
        pygame.display.flip() # Refresh display
        dt = clock.tick(60) / 1000 #limits FPS to 60
        
if __name__ == "__main__":
    main()