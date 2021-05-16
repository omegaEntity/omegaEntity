import pygame.font


class scoreboard:
    def __init__(self, settings, screen, stats):
        """initialize the score keeping attributes"""
        self.settings = settings
        self.screen = screen
        self.stats = stats
        self.screen_rect = self.screen.get_rect()

        #font settings for showing information
        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 48)

        #make the initial score image
        self.prep_score_image()
        self.prep_high_score_image()
        self.prep_level()
        self.ship_left()

    def prep_score_image(self):
        """turning the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bgColor)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 80
        self.score_image_rect.top = 20
        self.rounded_score = int(round(self.stats.score))
        self.score_str = "{:,}".format(self.rounded_score)
        self.score_str = str(self.score_str)

    def show_score(self):
        """showing the score"""
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.settings.bgColor)
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.ships_number_image, self.ships_number_image_rect)

    def prep_high_score_image(self):
        self.high_score = self.stats.high_score
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bgColor)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.screen_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bgColor)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.top = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom

    def ship_left(self):
        self.ships_number = self.stats.ships_left
        self.sentence = "ships left: "
        self.ships_number_str = str(self.sentence + str(self.ships_number))
        self.color = (0, 0, 255)
        self.ships_number_image = self.font.render(self.ships_number_str, True, self.color, self.settings.bgColor)
        self.ships_number_image_rect = self.ships_number_image.get_rect()
        self.ships_number_image_rect.bottom = self.screen_rect.bottom - 50
        self.ships_number_image_rect.left= self.screen_rect.left + 150

