import sys
import pygame


class AlienInvasion:
    def __init__(self):
        """Initialize game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyword and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()

            # Customizing for 60 Frames per second
            self.clock.tick(60)


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
