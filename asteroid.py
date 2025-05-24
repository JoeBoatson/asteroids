from circleshape import *
import random
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = velocity

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", center, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_velocity1 = self.velocity.rotate(random_angle)
            asteroid_velocity2 = self.velocity.rotate(-random_angle)
            
            new_asteroid1 = Asteroid(int(self.position.x), int(self.position.y), new_radius, (asteroid_velocity1 * 1.2))
            new_asteroid2 = Asteroid(int(self.position.x), int(self.position.y), new_radius, (asteroid_velocity2 * 1.2))
            return [new_asteroid1, new_asteroid2]
