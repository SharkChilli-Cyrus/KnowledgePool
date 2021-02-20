import pygame

class Ship():
    """Class Description"""

    def __init__(self, defaultSettings, screen):
        """Function Description"""
        self.screen = screen
        self.defaultSettings = defaultSettings
    
        self.image = pygame.image.load("images/ship.bmp") # load ship image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put the ship on the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.screen_rect.bottom - 30

        # self.center = float(self.rect.centerx)
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # move
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Function Description"""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.centerx += self.defaultSettings.shipSpeedFactor
        if self.moving_left == True and self.rect.left > 0:
            self.centerx -= self.defaultSettings.shipSpeedFactor
        
        # Top Left: (0, 0), Bottom Right: (+x, +y)
        if self.moving_up == True and self.rect.top > 20:
            self.centery -= self.defaultSettings.shipSpeedFactor
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom - 20:
            self.centery += self.defaultSettings.shipSpeedFactor
        
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Function Description"""
        self.screen.blit(self.image, self.rect)