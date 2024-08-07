import pygame.font


class SpaceInfoTexT:
    """This class is created to inform the user that space key can start the game"""
    def __init__(self, ai_main):
        """initialize the attributes of the SpaceInfoText"""
        self.screen = ai_main.screen
        self.screen_rect = self.screen.get_rect()

        # set the properties and dimensions of the info text
        self.width, self.height = 1000, 50
        self.text_bg_color = (230, 230, 230)
        self.text_color = (128, 128, 128)
        self.font = pygame.font.SysFont(None, 48)

        # create the info rect and position it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop

        self._prep_msg()

    def _prep_msg(self, msg="You can start the game with \"Space\" key."):
        """This renders the image of text, centers the image_rect to the rect"""
        self.text_image = self.font.render(msg, True, self.text_color, self.text_bg_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_text(self):
        """draw the text image on the screen"""
        self.screen.fill(self.text_bg_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
