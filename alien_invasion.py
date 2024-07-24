import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        """Initialize game, and create game resources."""
        pygame.init()
        self.Settings = Settings()

        self.screen = pygame.display.set_mode((self.Settings.screen_width, self.Settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            # calls the helper methods
            self._check_events()
            self.ship.update()
            self._update_screen()

            # Customizing for 60 Frames per second
            self.clock.tick(80)

    def _check_events(self):
        """Watch for keyword and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on screen and flip to new screen"""
        self.screen.fill(self.Settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
