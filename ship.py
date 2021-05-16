import pygame

class ship:
    def __init__(self, screen, settings):
        self.screen = screen
        self.image = pygame.image.load("E:/New folder (4)/ship.bmp")
        self.settings = settings
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom
        self.moveleft = False
        self.moveup = False
        self.moveright = False
        self.movedown = False
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def DrawCurrentShip(self):
        """prints the current position of ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """updates the changes"""

        if self.moveright and self.centerx < self.screen_rect.right: self.centerx += self.settings.ship_speed
        elif self.moveleft and self.centerx > self.screen_rect.left: self.centerx -= self.settings.ship_speed
        elif self.moveup and self.centery > self.screen_rect.top: self.centery -= self.settings.ship_speed
        elif self.movedown and self.centery < self.screen_rect.bottom: self.centery += self.settings.ship_speed
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def ship_center(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom
