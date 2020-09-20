# -*- coding: utf-8-sig -*-
# 
# $ brew install hg sdl sdl_image sdl_ttf sdl_mixer portmidi

import sys
import os

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
    This is a function description
    """
    pygame.init()

    defaultSettings = Settings()
    screen = pygame.display.set_mode(
        (defaultSettings.screenWidth, defaultSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(defaultSettings, screen)

    # create a container to save bullets
    bullets = Group()

    while True:
        gf.check_events(defaultSettings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(defaultSettings, screen, ship, bullets)



rootPath = os.path.dirname(os.path.abspath(__file__))
originalPath = os.getcwd()
os.chdir(rootPath)
workingPath = os.getcwd()

startInfo = """
===== Start Info =====
* Root Path:
    - {root_path}
* Original Working Path: 
    - {original_path}
* Changed Working Path: 
    - {working_path}
======================
""".format(root_path = rootPath, original_path = originalPath, working_path = workingPath)
print(startInfo)

run_game()