# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:31:29 2018

@author: mikke
"""
import requests

class Leaderboard:
    def __init__(self, game):
        self.game = game
        self.host = 'https://api.nicklas.io'
        
    
    def get_scores(self):
        params = dict(
            game=self.game
        )

        r = requests.get(self.host, params=params)
        return r.json()
    
    def new_score(self, user, score):
        params = dict(
            game=self.game,
            user=user,
            score=score
        )

        r = requests.post(self.host, json=params)
        return r.json()