import pygame
import math
from player import Player
from environment import Environment
from random import randint
from inputBox import InputBox
from highscore import Leaderboard

class Game:
        def __init__(self):
            self.state = 0
            #State 0: Menu
            #State 1: Game
            #State 2: Pause
            #State 3: Game_Over
            self.p = Player()
            self.e = Environment()
            self.l = Leaderboard('SlimesNStuff')
            self.ib = None
            
            self.points = 0
            self.target = [250, 250]
            
            self.scores = []
            
               
        def tick(self, pg, pressed):
            if math.sqrt((self.target[0] - self.p.x)**2 + (self.target[1] - self.p.y)**2) < 40:
                self.points += 1
                self.target = [randint(0,800), randint(0,600)]
        
        def start_game(self):
            if self.state == 0:
                self.state = 1     
                self.points = 0
                
                self.p.x = 100
                self.p.y = 100
                
                self.p.lives = 3
                self.p.state = 0
                self.p.HP = 100.0
                self.p.stateTime = 0
                self.p.vMovement = 0.0
                    
                self.target = [randint(0,800), randint(0,600)]

        def end_game(self):
            if self.state > 0:
                self.state = 0

        def toggle_pause(self):
            if self.state == 1:
                self.state = 2
            else:
                self.state = 1

        def started(self):
            if self.state > 0:
                return True
            else:
                return False
            
def draw_game():
    #Menu
    if game.state == 0:
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (30,30,30), pygame.Rect(360, 280, 80, 50))
        screen.blit(myfont.render("MENU", 1, (255,255,255)), (379, 292))
        screen.blit(myfont.render("Press 'Esc' to start", 1, (255,255,255)), (290, 335))
   
    #Playing
    elif game.state == 1:
                
        #environment
        screen.blit(game.e.bg,(0,0))
        
        for i in range(len(game.e.level4)):
            for j in range(len(game.e.level4[0])):
                if game.e.level4[i][j] == 1:
                    screen.blit(game.e.platforms[0], (i*32,j*32))
    
        #Player
        if game.p.state == 1:
            sprite = game.p.sprites[3]
        elif game.p.state == 2:
            game.state = 3
            game.scores = game.l.get_scores()['scores']
            sprite = game.p.sprites[3]
            game.ib = InputBox(60,370,30,30)
        elif game.p.up:
            sprite = game.p.sprites[4+int(pygame.time.get_ticks()/200)%2]
        elif game.p.down:
            sprite = game.p.sprites[6+int(pygame.time.get_ticks()/200)%2]
        elif game.p.right:
            sprite = game.p.sprites[8+int(pygame.time.get_ticks()/200)%2]
        elif game.p.left:
            sprite = game.p.sprites[10+int(pygame.time.get_ticks()/200)%2]
        else:
            sprite = game.p.sprites[int(pygame.time.get_ticks()/300)%2]
        hw = [sprite.get_width(),sprite.get_height()]
        sprite = pygame.transform.scale(sprite,(hw[0]*4,hw[1]*4))
        screen.blit(sprite, (game.p.x - hw[0]*2, game.p.y - hw[1]*3.5))
        
        #Player lives
        lSprite = game.p.sprites[int(pygame.time.get_ticks()/300)%2]
        lives = pygame.transform.scale(game.p.sprites[0],(lSprite.get_width()*2,lSprite.get_height()*2))
        for i in range(0,game.p.lives):
            screen.blit(lives,(10+i*35,10))
        
        #Target
        pygame.draw.rect(screen, (123,50,10), pygame.Rect(game.target[0]-25, game.target[1]-50, 50, 50))
        
        #Points
        screen.blit(myfont.render("Points: {}".format(game.points), 1, (255,0,0)), (100, 100))
        
    #Pause   
    elif game.state == 2:
        pygame.draw.rect(screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
        screen.blit(myfont.render("PAUSE", 1, (255,255,255)), (400, 300))
        
        
    #Game_over    
    elif game.state ==3:
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(10,10,10), pygame.Rect(40,40,720,560))
        screen.blit(myfont.render("Press 'Esc' to exit to menu", 1, (255,255,255)), (440, 570))
        
        #Title
        screen.blit(HSfont.render("GAME OVER", 1, (255,255,255)), (300, 50))
        
        #Highscores
        pygame.draw.rect(screen,(0,0,0), pygame.Rect(395,160,212,400))
        pygame.draw.rect(screen,(5,5,5),pygame.Rect(607,160,120,400))
        screen.blit(HSfont.render("Highscores", 1, (255,255,255)), (450, 120))
        screen.blit(Mfont.render("Name        Score",1,(255,255,255)),(432,165))
        
        if len(game.scores)>10:
            for i in range(0,10):
                screen.blit(myfont.render("{}: {}".format(i+1,game.scores[i]['user']),1,(255,255,255)),(400,190+i*30))
                screen.blit(myfont.render("{}".format(game.scores[i]['score']),1,(255,255,255)),(613,190+i*30))
        else:
            for i in range(len(game.scores)):
                screen.blit(myfont.render("{}: {}".format(i+1,game.scores[i]['user']),1,(255,255,255)),(400,190+i*30))
                screen.blit(myfont.render("{}".format(game.scores[i]['score']),1,(255,255,255)),(613,190+i*30))
        
        #Player
        #screen.blit(myfont.render("You are number: {}".format(?), 1, (255,255,255)), (60, 270))
        screen.blit(myfont.render("Score: {}".format(game.points), 1, (255,255,255)), (60, 300))
        screen.blit(myfont.render("Enter your name:", 1, (255,255,255)), (60, 350))
        #   Input
        game.ib.draw(screen)
        if pressed[pygame.K_RETURN]:
            name = str(game.ib.get_input())
            print(game.l.new_score(name,game.points))
            game.scores = game.l.get_scores()['scores']
            print(game.scores)
            game.points = 0

pygame.init()
screen = pygame.display.set_mode((800, 640))
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 18)
HSfont = pygame.font.SysFont("monospace",40)
Mfont = pygame.font.SysFont("monospace",25)

done = False

game = Game()
    
clock = pygame.time.Clock()

while not done:
    ticktime = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if game.state == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            game.toggle_pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game.started():
                game.end_game()
            else:
                game.start_game()
        if game.state == 3:
            game.ib.handle_event(event)
        if game.state == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            game.p.lives = -1
    
    pressed = pygame.key.get_pressed()


    if game.state == 3:
        game.ib.update()
        
    if game.state == 1:
        game.p.tick(pygame,pressed, ticktime)    
    game.tick(pygame, pressed)
    
    draw_game()
    
    pygame.display.flip()
    

