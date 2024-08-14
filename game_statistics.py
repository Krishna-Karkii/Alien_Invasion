class GameStats:
    """This class handles everything related to scores and ship count"""
    def __init__(self, ai_game):
        """initialize statistics of the game."""
        self.settings = ai_game.Settings
        self.reset_stats()
        self._get_high_score()

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def check_high_score(self):
        """check if the current score is greater than high score,
        and write it in highscore file."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))

    def _get_high_score(self):
        """get the high score from file."""
        with open("highscore.txt", "r") as file:
            self.high_score = int(file.read())
