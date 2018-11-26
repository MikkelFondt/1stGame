# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:31:29 2018

@author: mikke
"""
import sqlite3

class Highscore:
    
    def __init__(self):
        self.conn = sqlite3.connect('highscores.db')
        
        self.cursor = self.conn.cursor()
        
        try:
            #self.cursor.execute("DROP TABLE highscore;")

            self.cursor.execute('''
                        CREATE TABLE highscore (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT,
                        Score INTEGER
                        );
                        ''')
        except:
            pass
    
    def add_score(self,Name,Score):
        self.cursor.execute('''INSERT INTO employees
                       (Name, Salary) 
                       VALUES
                       ('?', ?);''',(Name,Score))
        self.conn.commit()
    
    #def find_number(Score):
    

    def get_top10(self):
        self.cursor.execute('''SELECT * FROM highscore 
                            ORDER BY Score DESC
                            LIMIT 10;''')
        l = []
        for i in self.cursor:
            l.append(i[0],i[1])
    