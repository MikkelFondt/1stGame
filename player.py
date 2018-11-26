# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:18:02 2018

@author: mikke
"""
import pygame
from environment import Environment

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        
        self.e = Environment()
        
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        
        self.HP = 100.0
        self.lives = 3
        
        #0 = alive, 1 = dead, 
        self.state = 0
        self.stateTime = 0
        
        #0 = onGround, 1 = jumping, 2 = Falling
        self.jState = 2
        self.jumpTime = 0
        
        self.squich = False
        
        self.vMovement = 0.0
        
        
        try:
            #.convert() converterer billedet til det format, der
            #er valgt med pyamge.display.setmode(). Hurtigere tegning hver gang
            self.sheet = pygame.image.load("FullGreenSlimes.png").convert()
        except pygame.error:
            pass
        
         #   Stå1        Stå2            Jordsplat   Død             
        rects = ((4,8,16,10), (36,7,16,11), (67,0,18,19), (97,3,22,14), 
                #     Op1         Op2             Fald1           Fald2
                 (5,26,14,13), (37,26,14,16), (69,28,14,13), (101,25,14,16), 
                #   GåVenstre1  GåVenstre2      GåHøjre1        GåHøjre2
                 (4,49,17,11), (36,49,17,11), (69,49,17,11), (101,49,17,11))
        self.sprites = []
        for r in rects:
            image = pygame.Surface(pygame.Rect(r).size).convert() 
            image.set_colorkey((0,0,0))
            image.blit(self.sheet, (0, 0), pygame.Rect(r))
            self.sprites.append(image)
                
    def tick(self, pg, pressed,ticktime):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        
        if self.state == 1:
            self.stateTime += ticktime
            if self.stateTime > 700:
                self.state = 0
                self.y = 100
                self.x = 100
                self.HP = 100.0
                self.stateTime = 0
                self.vMovement = 0.0
                self.lives -= 1
            
        
        #Vertical movement
        if self.jState == 0:
            
            if pressed[pg.K_UP]:
                self.jState = 1
            
            self.ctrl_p()
            if self.e.find_col(self.x,self.y) ==False:
                self.jState=2
            
        
        if self.jState == 1 and self.jumpTime< 10:
            if pressed[pg.K_UP]:
                self.jumpTime += 1
                self.y -= 20
                self.up = True
                if self.jumpTime >= 10:
                    self.jumpTime = 0
                    self.jState = 2 
                    self.vMovement = 13
            else:
                self.jumpTime = 0
                self.jState = 2
                self.vMovement = 13
                
        if self.jState == 2:
            if self.vMovement > 5:
                self.up = True
            elif self.vMovement < -5:
                self.down = True
                
            self.y -= self.vMovement
            self.vMovement -= 0.5*float(ticktime)/16
            if self.vMovement > 30:
                self.vMovement = 30
            
            self.ctrl_p()
            if self.e.find_col(self.x,self.y) ==True and self.vMovement<0:
                self.y = int(self.y/32)*32
                self.vMovement = 0
                self.jState = 0
        
        #Horizontal movement
        if pressed[pg.K_LEFT]: 
            self.x -= 4*float(ticktime)/16
            self.left = True
        if pressed[pg.K_RIGHT]: 
            self.x += 4*float(ticktime)/16
            self.right = True
        
        
    def ctrl_p(self):
        if self.x < 0:
            self.x = 0
        if self.x > 790:
            self.x = 790
            
        if self.y < 10:
            self.y = 10
        if self.y > 640:
            self.y = 640
            self.HP = 0
            self.state = 1
    
    