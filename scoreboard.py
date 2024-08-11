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

        # prepare the initial score, and high score image
        self.prep_score()
        self.prep_high_score()

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

    def prep_high_score(self):
        """prepare the high score image and
        set its position respective to the window."""
        # round the high score to the nearest 10 and give commas to score
        self.stats.high_score = round(self.stats.high_score, -1)
        high_score = f"High_Score: {self.stats.high_score:,}"

        self.highscore_img = self.font.render(high_score, True, self.font_color)

        # position the high score at the middle of the window
        self.highscore_img_rect = self.highscore_img.get_rect()
        self.highscore_img_rect.centerx = self.screen_rect.centerx
        self.highscore_img_rect.top = self.score_img_rect.top

    def draw_high_score(self):
        """draw the high score to the surface in its defined position"""
        self.screen.blit(self.highscore_img, self.highscore_img_rect)
