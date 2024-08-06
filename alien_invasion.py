import sys
import pygame
import time

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_statistics import GameStats


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

        self.game_stats = GameStats(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            # call the methods required in main loop
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
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
        self.aliens.draw(self.screen)
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

        # create condition to allow the numbers of bullets_allowed in settings
        if len(self.bullets) < self.Settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_alien_collisions(self):
        """Respond to bullet alien collisions."""
        # check for any bullets that have hit aliens.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_bullets(self):
        """manages the bullets in the screen"""
        self.bullets.update()

        # remove unnecessary bullets for bullets group
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _create_fleet(self):
        """create the fleet of alien"""
        # create an alien and keep adding until no room left
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        # add the alien until the condition met, leaving 7 alien height space
        while current_y < (self.Settings.screen_height - 7 * alien_height):
            while current_x < (self.Settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # reset the current_x, increment the value of current_y
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, position_x, position_y):
        """create an alien and add the alien in the group"""
        new_alien = Alien(self)
        new_alien.x = position_x
        new_alien.rect.x = position_x
        new_alien.rect.y = position_y
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """check if the fleet has hit edge"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """change fleet direction if fleet has hit the edge"""
        """fleet dropdown if the fleet hit the edge"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.Settings.fleet_dropdown
        self.Settings.fleet_direction *= -1

    def _ship_hit(self):
        """This method handles necessary tasks after ship is hit"""
        self.game_stats.ships_left -= 1

        # empty the aliens and bullets after the ship is hit
        self.aliens.empty()
        self.bullets.empty()

        # create new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        time.sleep(0.5)

    def _update_alien(self):
        """update alien fleet movement"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
