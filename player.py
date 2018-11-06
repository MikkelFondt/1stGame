# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:18:02 2018

@author: mikke
"""
import pygame

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.onGround = False
        self.squich = False
        self.vMovement = 0.0
        
        try:
            #.convert() converterer billedet til det format, der
            #er valgt med pyamge.display.setmode(). Hurtigere tegning hver gang
            self.sheet = pygame.image.load("FullGreenSlimes.png").convert()
        except pygame.error:
            pass
        
         #   Stå1        Stå2            Jordsplat   Død             
        rects = ((4,8,16,10), (36,7,16,11), (67,0,18,19), (97,0,22,19), 
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
                
    def tick(self, pg, pressed):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        if pressed[pg.K_UP]: #and dist to ground < ? (lav også det til +=)
            self.vMovement =20
        if pressed[pg.K_LEFT]: 
            self.x -= 3
            self.left = True
        if pressed[pg.K_RIGHT]: 
            self.x += 3
            self.right = True
        
        self.y -= self.vMovement
        self.vMovement -= 2
        
        if self.y > 578:
            self.vMovement = 0
            self.y = 578
        
        if self.vMovement > 5:
            self.up = True
        elif self.vMovement < -5:
            self.down = True
        
        