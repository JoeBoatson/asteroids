import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0

    all_shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (all_shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("black") # fill screen with black

        updatable.update(dt)
        for d in drawable:
            d.draw(screen) # draw the player
        
        for a in all_asteroids:
             if a.collision(player) == True:
                print("Game over!")
                sys.exit()
        pygame.display.flip() # Refresh display
        dt = clock.tick(60) / 1000 #limits FPS to 60
        
if __name__ == "__main__":
    main()