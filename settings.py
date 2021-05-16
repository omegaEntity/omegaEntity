class settings:
    def __init__(self):
        self.screenwidth = 1000
        self.screenheight = 700
        self.bgColor = (230, 230, 230)
        #bullets settings
        self.bullet_height = 15
        self.bullet_width = 5
        self.bullet_color = 0, 0, 0
        self.bullet_speed_factor = 2
        self.numberOfBullets = 3
        self.alien_speed = 0.3
        self.fleet_direction = 1
        self.fleet_dropping_speed = 10
        self.ship_limit = 3
        self.speed_up_scale = 1.1
        self.score_speed_up_scale = 1.5
        self.ship_speed = 5
        self.score_per_alien = 20

    def initialize_dynamic_settings(self):
        self.ship_speed = 2
        self.bullet_speed_factor = 2
        self.alien_speed = 0.3



    def increase_speed(self):
        """increases the speed as well as the score for each alien hit"""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.score_per_alien *= int(self.score_speed_up_scale)