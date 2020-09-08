# -*- coding: utf-8-sig -*-
# 
# $ brew install hg sdl sdl_image sdl_ttf sdl_mixer portmidi

import sys
import os

import pygame


class Settings():
    """
    This is a class description
    """

    def __init__(self):
        """Initiate Settings"""

        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)



def run_game():
    """
    This is a function description
    """

    pygame.init()
    defaultSettings = Settings()
    screen = pygame.display.set_mode(
        (defaultSettings.screenWidth, defaultSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(defaultSettings.bgColor)
        pygame.display.flip()



run_game()
