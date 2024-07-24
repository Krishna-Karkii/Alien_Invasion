import pygame


class Ship:
    """This class manages the ship"""
    def __init__(self, ai_main):
        """Initial the ship and its starting position"""
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
        if self.moving_right:
            self.x += self.settings.speed

        if self.moving_left:
            self.x -= self.settings.speed

        self.rect.x = self.x
