class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # alien settings
        self.fleet_dropdown = 10.0

        # Game statistics Settings
        self.ship_limit = 3

        self.speed_up_scale = 1.25

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize the dynamic values of the game"""
        self.ship_speed = 2
        self.alien_speed = 1.5
        self.bullet_speed = 2.5

        # -1 for the left direction, 1 for the right direction
        self.fleet_direction = 1.0

