import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """This class manages the bullet fired from ship"""
    def __init__(self, ai_main):
        """Create a bullet object at ship's current position"""
        super().__init__()
        self.screen = ai_main.screen
        self.settings = ai_main.Settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect((0, 0), self.settings.bullet_width, self.settings.screen_height)
        self.rect.midtop = ai_main.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

