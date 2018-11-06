# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:22:51 2018

@author: mikke
"""

import pygame

class Environment:
    def __init__(self):
        self.level = 0
        self.bg = pygame.image.load('bg.jpg')
        self.platforms = [pygame.image.load('tile_00.png'),pygame.image.load('tile_01.png'),pygame.image.load('tile_02.png')]
        self.level1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] for i in range(25)]
#    def design_level():
#        a = 0
#        if self.level == 0:
            