import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in a fleet"""
    def __init__(self, ai_main):
        """initialize the alien and its starting position"""
        super().__init__()
        self.screen = ai_main.screen
        self.settings = ai_main.Settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien at top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """update the position of the alien"""
        self.x += self.settings.alien_speed

        self.rect.x = self.x

