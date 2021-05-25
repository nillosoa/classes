
class Settings():
    """ A class to store all settings for Alien Invasion """
    def initialize_dynamic_setttings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)

    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = int(1360 / 1.5) 
        self.screen_height = int(768 / 1.2)
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3

        # Bullet setttings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point value increase
        self.score_scale = 1.5

        self.initialize_dynamic_setttings()
