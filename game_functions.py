import pygame
import sys
from bullets import Bullets
from alien import Alien
from time import sleep

def check(settings, screen, ship1, T_bullets, play_button, stats, aliens):
    """checks the user controls"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, settings, screen, ship1, T_bullets)
        elif event.type == pygame.KEYUP:
            check_key_up(event, ship1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ship1, screen, aliens, T_bullets, settings)

def check_play_button(stats, play_button, mouse_x, mouse_y, ship, screen, aliens, T_bullets, settings):
    button_is_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_is_clicked and not stats.game_running:
        #hide the mouse cursor
        pygame.mouse.set_visible(False)
        #reset the game's stats
        stats.reset_stats()
        stats.game_running = True
        #empty the list of Aliens as well as bullets
        aliens.empty()
        T_bullets.empty()

        #creating a fleet and centring the ship
        create_fleet(settings, screen, ship, aliens)
        ship.ship_center()

def check_keydown(event, settings, screen, ship1, T_bullets):
    """for keydown"""
    if event.key == pygame.K_RIGHT:
        ship1.moveright = True
    elif event.key == pygame.K_LEFT:
        ship1.moveleft = True
    elif event.key == pygame.K_UP:
        ship1.moveup = True
    elif event.key == pygame.K_DOWN:
        ship1.movedown = True
    elif event.key == pygame.K_SPACE:
        fireBullets(settings, screen, ship1, T_bullets)


def check_key_up(event, ship1):
    """for keyup"""
    if event.key == pygame.K_LEFT:
        ship1.moveleft = False
    elif event.key == pygame.K_RIGHT:
        ship1.moveright = False
    elif event.key == pygame.K_UP:
        ship1.moveup = False
    elif event.key == pygame.K_DOWN:
        ship1.movedown = False


def updateTheScreen(settings, screen, ship, T_bullets, aliens, stats, play_button, sb):
    screen.fill(settings.bgColor)
    ship.DrawCurrentShip()
    aliens.draw(screen)
    sb.show_score()
    check_high_score(stats, sb)
    for bullets in T_bullets.sprites():
        bullets.draw_bullet()
    if not stats.game_running:
        play_button.draw_button()
    pygame.display.flip()


def updateBullets(aliens, T_bullets, settings, screen, ship, stats, sb):
    for bullet in T_bullets.copy():
        if bullet.rect.bottom <= 0:
            T_bullets.remove(bullet)

    collision = pygame.sprite.groupcollide(aliens, T_bullets, True, True)
    if collision:
        stats.score += settings.score_per_alien
        sb.prep_score_image()
    if len(aliens) == 0 :
        T_bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(settings, screen, ship, aliens)

def check_high_score(stats, sb):
    if stats.high_score < stats.score:
        stats.high_score = stats.score
        sb.prep_high_score_image()

def fireBullets(settings, screen, ship, T_bullets):
    if len(T_bullets) < settings.numberOfBullets:
        new_bullet = Bullets(settings, ship, screen)
        T_bullets.add(new_bullet)


def create_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens = get_number_of_aliens(settings, alien_width)
    number_rows = get_number_of_rows(settings, ship.rect.height, alien_width)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            create_alien(settings, screen, alien_width, aliens, row_number, alien_number)


def get_number_of_aliens(settings, alien_width):
    available_space_x = settings.screenwidth - (2 * alien_width)
    number_aliens = int(available_space_x / (2 * alien_width))
    return number_aliens


def get_number_of_rows(settings, ship_height, alien_height):
    available_space_y = settings.screenheight - ship_height - (3 * alien_height)
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows


def create_alien(settings, screen, alien_width, aliens, row_number, alien_number):
    alien = Alien(settings, screen)
    alien.x = (2 * alien_width * alien_number) + alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien_width * row_number
    aliens.add(alien)


def update_aliens(aliens, settings, ship, T_bullets, stats, screen, sb):
    check_fleet_egdes(aliens, settings)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ship, aliens, T_bullets, stats, settings,screen, sb)
    check_aliens_touch_bottom(ship, aliens, T_bullets, stats, screen, settings, sb)

def check_fleet_egdes(aliens, settings):
    """checks the direction of the fleet and appropriately handles it."""
    for alien in aliens.sprites():
        if (alien.check_edges()) :
            change_fleet_direction(aliens, settings)
            break


def change_fleet_direction(aliens, settings):
    """changes the fleet direction and also drops it."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_dropping_speed
    settings.fleet_direction *= -1


def ship_hit(ship, aliens, T_bullets, stats, settings, screen, sb):
    """decrement the number of ships"""
    stats.ships_left -= 1
    sb.ship_left()
    """empty all the aliens fleets and bullets"""
    aliens.empty()
    T_bullets.empty()

    """freeze the screen momentarily"""
    sleep(0.7)

    """create new aliens and draw the ship at the centre"""
    create_fleet(settings, screen, ship, aliens)
    ship.ship_center()
    """terminating the game when user runs out of ships"""
    if stats.ships_left == 0 :
        stats.game_running = False
        pygame.mouse.set_visible(True)
        stats.score = 0
    """resetting the game's difficulty"""
    settings.initialize_dynamic_settings()

def check_aliens_touch_bottom(ship, aliens, T_bullets, stats, screen, settings, sb):
    """check if any alien has touched the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens :
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ship, aliens, T_bullets, stats, settings, screen, sb)
            break





