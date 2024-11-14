import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Draw an asteroid using a circle
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt):
        # Move asteroid in a straight line
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
                return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector_1 * 1.2
        asteroid2.velocity = new_vector_2 * 1.2