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
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()

            elif self.event.type == pygame.KEYDOWN:
                self._check_keydown()

            elif self.event.type == pygame.KEYUP:
                self._check_keyup()

    def _update_screen(self):
        """Update images on screen and flip to new screen"""
        self.screen.fill(self.Settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def _check_keydown(self):
        """checks for event related to keydown"""
        if self.event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif self.event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup(self):
        """checks for event related to keydown"""
        if self.event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if self.event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
