import sys
import pygame

from ship import Ship
from alien import Alien
from bullet import Bullet


def get_number_aliens_x(defaultSettings, alien_width):
    available_space_x = defaultSettings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    return number_aliens_x


def get_number_rows(defaultSettings, ship_height, alien_height):
    available_space_y = defaultSettings.screen_height - 2 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows


def create_alien(defaultSettings, screen, aliens, alien_number, row_number):
    alien = Alien(defaultSettings, screen)
    
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(defaultSettings, screen, ship, aliens):
    alien = Alien(defaultSettings, screen)
    number_aliens_x = get_number_aliens_x(defaultSettings, alien.rect.width)
    number_rows = get_number_rows(defaultSettings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(defaultSettings, screen, aliens, alien_number, row_number)
        



def fire_bullet(defaultSettings, screen, ship, bullets):
    """Function Description"""
    if len(bullets) < defaultSettings.bulletsAllowed:
        # create a bullet and add it into the group bullets
        new_bullet = Bullet(defaultSettings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, defaultSettings, screen, ship, bullets):
    """Key Down"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    
    elif event.key == pygame.K_SPACE:
        fire_bullet(defaultSettings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    


def check_events(defaultSettings, screen, ship, bullets):
    """Recording keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, defaultSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(defaultSettings, screen, ship, aliens, bullets):
    """Function Description"""

    screen.fill(defaultSettings.bgColor)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(bullets):
    """Change bullets' positions and delete missed bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def change_fleet_direction(defaultSettings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += defaultSettings.fleet_drop_speed
    defaultSettings.fleet_direction *= -1


def check_fleet_edges(defaultSettings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(defaultSettings, aliens)
            break


def update_aliens(defaultSettings, aliens):
    check_fleet_edges(defaultSettings, aliens)
    aliens.update()