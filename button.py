import pygame.font


class Button:
    """This class creates a button, which when clicked initiate the start of a new game"""
    def __init__(self, ai_main, msg):
        """initialize the attributes of button class"""
        self.screen = ai_main.screen
        self.screen_rect = ai_main.screen.get_rect()

        # define the properties of the button and font
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # create rect and centralize it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """This method renders a msg image, centers it to the buttons rect"""
        # set the position for easy and expert buttons
        if msg == "Easy":
            self.easy()
        elif msg == "Expert":
            self.expert()

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def easy(self):
        """start the game in most basic level and pace up."""
        self.x, self.y = self.rect.center
        self.y -= 100
        self.rect.center = (self.x, self.y)

    def expert(self):
        """start the game in hard level and pace up."""
        self.x, self.y = self.rect.center
        self.y += 100
        self.rect.center = (self.x, self.y)
