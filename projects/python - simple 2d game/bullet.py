import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class Description"""

    def __init__(self, defaultSettings, screen, ship):
        """Function Description"""
        super().__init__()
        self.screen = screen

        # create a new bullet at (0, 0)
        self.rect = pygame.Rect(0, 0, 
                            defaultSettings.bulletWidth, defaultSettings.bulletHeight)
        # move the new bullet to the right position
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = defaultSettings.bulletColor
        self.speed_factor = defaultSettings.bulletSpeedFactor
    
    def update(self):
        # - means up
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)