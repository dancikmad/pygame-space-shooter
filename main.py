import pygame
import constants as c
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    pygame.display.set_caption("Triangle Game")
    clock = pygame.time.Clock()

    # Create player outside the game loop
    x = c.SCREEN_WIDTH / 2
    y = c.SCREEN_HEIGHT / 2
    player = Player(x, y)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get time delta
        dt = clock.tick(60) / 1000

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw player
        player.draw(screen)

        player.update(dt)
        # Update display
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
