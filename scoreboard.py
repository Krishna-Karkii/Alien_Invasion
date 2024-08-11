import pygame.font


class ScoreBoard:
    """This class is related to the score of the game."""
    def __init__(self, ai_game):
        """initialize the attributes of the scoreboard."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.game_stats

        # properties of the scoreboard rect
        self.font_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial scores image
        self.prep_score()

    def prep_score(self):
        """prepare the score image to display on the window."""
        # round the score to the nearest 10 and give appropriate commas
        self.stats.score = round(self.stats.score, -1)
        score = f"Score: {self.stats.score:,}"

        self.score_img = self.font.render(score, True, self.font_color)

        # position the image rect top-right to window top-right
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def draw_score(self):
        """draw the score image to its defined rect."""
        self.screen.blit(self.score_img, self.score_img_rect)
