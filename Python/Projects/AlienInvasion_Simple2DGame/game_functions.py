import sys
import pygame

from bullet import Bullet
            
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


def update_screen(defaultSettings, screen, ship, bullets):
    """Function Description"""

    screen.fill(defaultSettings.bgColor)
    # ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()


def update_bullets(bullets):
    """Change bullets' positions and delete missed bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)