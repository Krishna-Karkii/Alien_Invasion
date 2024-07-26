import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        """Initialize game, and create game resources."""
        pygame.init()
        self.Settings = Settings()

        # create frame, get frame width, frame height,and set window title
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.Settings.screen_width = self.screen.get_width()
        self.Settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            # call the methods required in main loop
            self._check_events()
            self.ship.update()
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _check_keydown(self):
        """checks for event related to keydown"""
        if self.event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif self.event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif self.event.key == pygame.K_q:
            sys.exit()
        elif self.event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self):
        """checks for event related to keydown"""
        if self.event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if self.event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a bullet instance and add into bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
