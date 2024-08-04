class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship speed
        self.speed = 2

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # alien settings
        self.alien_speed = 1.0
        self.fleet_dropdown = 10.0
        # -1 for the left direction, 1 for the right direction
        self.fleet_direction = 1.0

        # Game statistics Settings
        self.ship_limit = 3
