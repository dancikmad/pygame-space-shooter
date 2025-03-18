import sys

import pygame

import constants as c
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player, Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_filed = AsteroidField()
    Player.containers = (updatable, drawable)

    # instantiate player
    x = c.SCREEN_WIDTH / 2
    y = c.SCREEN_HEIGHT / 2

    player = Player(x, y)

    dt = 0

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()

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
