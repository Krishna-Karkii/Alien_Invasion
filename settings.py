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
        self.alien_points_up = 1.5

        self.initialize_easy_dynamics()

    def speed_up(self):
        """speed up the overall game"""
        self.ship_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale

    def initialize_easy_dynamics(self):
        """initialize the easy difficulty dynamics"""
        self.ship_speed = 2.0
        self.alien_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_points = 10

        # -1 for the left direction, 1 for the right direction
        self.fleet_direction = 1.0

    def initialize_medium_dynamics(self):
        """initialize the medium difficulty dynamics"""
        self.ship_speed = 3.0
        self.alien_speed = 2.0
        self.bullet_speed = 4

        # -1 for the left direction, 1 for the right direction
        self.fleet_direction = 1.0

    def initialize_expert_dynamics(self):
        """initialize the expert difficulty dynamics"""
        self.ship_speed = 4.0
        self.alien_speed = 2.5
        self.bullet_speed = 6

        # -1 for the left direction, 1 for the right direction
        self.fleet_direction = 1.0
