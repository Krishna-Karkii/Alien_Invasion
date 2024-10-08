import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """This class manages the ship"""
    def __init__(self, ai_main):
        """Initial the ship and its starting position"""
        super().__init__()
        self.screen = ai_main.screen
        self.settings = ai_main.Settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact position
        self.x = float(self.rect.x)

        # initializing the movement to be false
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the ship position based on movement flags."""

        # moving the ship right until the right edge, if right flag is true
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # moving the ship left until the left edge, if left flag is true
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """This method center the ship position"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
