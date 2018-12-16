# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:22:51 2018

@author: mikke
"""

import pygame

class Environment:
    def __init__(self):
        self.level = 0
        background = pygame.image.load('bg.jpg')
        self.bg = pygame.transform.scale(background, (800,640))
        
        self.platforms = [pygame.image.load('tile_00.png'),pygame.image.load('tile_01.png'),pygame.image.load('tile_02.png')]
        self.level1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] for i in range(25)]
        
        self.level2 = [[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1] for i in range(6)]
        for j in range(13):
            self.level2.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        for k in range(6):
            self.level2.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1])
            
        self.level3 = [[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1] for i in range(6)]
        for j in range(5):
            self.level3.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        for j in range(3):
            self.level3.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        for j in range(5):
            self.level3.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        for k in range(6):
            self.level3.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1])
            
        
        self.level4 = [[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1] for i in range(6)]
        for j in range(5):
            self.level4.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        for j in range(3):
            self.level4.append([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        for j in range(5):
            self.level4.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        for k in range(6):
            self.level4.append([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
                       
    def find_col(self,x,y): 
#Midlertidlig
#        try:
#            if self.level4[int(x/32)][int(y/32)] == 1:
#                return True
#            else: 
#                return False
#        except:
#            return False
            
        if 0 <= int(x/32) < len(self.level4) and 0 <= int(y/32) < len(self.level4[0]):
            if self.level4[int(x/32)][int(y/32)] == 1:
                return True
            else: 
                return False
        else:
            return False
              
#    def design_level():
#        a = 0
#        if self.level == 0:
            