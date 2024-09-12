import pygame.draw
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.containers = []
        self.velocity = pygame.Vector2(0, 0)  # Initialize with zero velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(rand_angle)
            v2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            shard = Asteroid(self.position.x, self.position.y, new_radius)
            debris = Asteroid(self.position.x, self.position.y, new_radius)
            shard.velocity = v1 * 1.2
            debris.velocity = v2 * 1.2

