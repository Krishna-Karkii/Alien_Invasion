class GameStats:
    """This class handles everything related to scores and ship count"""
    def __init__(self, ai_game):
        """initialize statistics of the game."""
        self.settings = ai_game.Settings
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
