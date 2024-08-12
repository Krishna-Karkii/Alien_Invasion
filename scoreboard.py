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

        # prepare the initial score, level and high score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

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

    def prep_level(self):
        """prepare the level image and
        set its position respective to the window."""
        level = f"Level: {self.stats.level}"
        self.level_img = self.font.render(level, True, self.font_color)

        # set the position of the level image
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.top = 70
        self.level_img_rect.right = self.screen_rect.right - 20

    def draw_score(self):
        """draw the images of the scores,and level."""
        # current score of the player
        self.screen.blit(self.score_img, self.score_img_rect)
        # high score of the player
        self.screen.blit(self.highscore_img, self.highscore_img_rect)
        # current level of the player
        self.screen.blit(self.level_img, self.level_img_rect)
