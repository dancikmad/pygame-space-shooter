import pygame
from circleshape import CircleShape
import constants as c
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        asteroid_1 = Asteroid(
            self.position.x, self.position.y, (self.radius - c.ASTEROID_MIN_RADIUS)
        )
        asteroid_2 = Asteroid(
            self.position.x, self.position.y, (self.radius - c.ASTEROID_MIN_RADIUS)
        )
        asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)
        asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)
