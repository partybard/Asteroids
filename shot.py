from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        # Draw an shot using a circle
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt):
        # Move shot in a straight line
        self.position += self.velocity * dt
