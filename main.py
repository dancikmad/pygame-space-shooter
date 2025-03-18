import pygame
from pygame.display import update
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create player outside the game loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    x = c.SCREEN_WIDTH / 2
    y = c.SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    dt = 0

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        # Clear screen
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        # Update display
        pygame.display.flip()

        # Get time delta
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
