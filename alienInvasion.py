
import pygame
import game_functions as gf
from settings import settings as s
from alien import Alien
from ship import ship
from pygame.sprite import Group
from gamestats import GameStats
from button import button
from scoreboard import scoreboard


def run_game() :
    pygame.init()
    Settings = s()

    screen = pygame.display.set_mode((Settings.screenwidth, Settings.screenheight))
    stats = GameStats(Settings)
    #making an alien
    alien = Alien(Settings, screen)
    play_button = button(screen , Settings, "play")
    sb = scoreboard(Settings, screen, stats)
    pygame.display.set_caption("Alien Invasion")
    ship1 = ship(screen, Settings)
    T_bullets = Group()
    aliens = Group()
    gf.create_fleet(Settings, screen,ship1,aliens)
    while True:
        gf.check(Settings,screen, ship1,  T_bullets, play_button , stats, aliens)
        gf.updateTheScreen(Settings, screen, ship1, T_bullets, aliens, stats, play_button, sb)
        if stats.game_running:
            ship1.update()
            T_bullets.update()
            gf.updateBullets(aliens, T_bullets, Settings, screen, ship1, stats, sb)
            gf.update_aliens(aliens, Settings ,ship1,T_bullets, stats, screen, sb)



run_game()