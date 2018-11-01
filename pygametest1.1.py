import pygame
import math
from random import randint

class Game:
        def __init__(self):
                self.state = 0
                #State 0: Menu
                #State 1: Game
                #State 2: Pause
                self.x = 100
                self.y = 100
                self.points = 0
                self.target = [250, 250]
                self.up = False
                self.down = False
                self.left = False
                self.right = False
                
                try:
                        #.convert() converterer billedet til det format, der
                        #er valgt med pyamge.display.setmode(). Hurtigere tegning hver gang
                        self.sheet = pygame.image.load("FullGreenSlimes.png").convert()
                except pygame.error:
                        pass
                            
                        #   Stå1        Stå2            Jordsplat   Død             
                rects = ((4,7,16,11), (36,7,16,11), (67,0,18,19), (97,0,22,19), 
                        #     Op1         Op2             Fald1           Fald2
                         (5,26,14,13), (37,26,14,16), (69,28,14,13), (101,25,14,16), 
                        #   GåVenstre1  GåVenstre2      GåHøjre1        GåHøjre2
                         (4,49,17,11), (36,49,17,11), (69,49,17,11), (101,49,17,11))
                self.sprites = []
                for r in rects:
                        image = pygame.Surface(pygame.Rect(r).size).convert()
                        image.blit(self.sheet, (0, 0), pygame.Rect(r))
                        self.sprites.append(image)


        def tick(self, pg, pressed):
                self.up = False
                self.down = False
                self.left = False
                self.right = False
                if self.state == 1:
                        if pressed[pg.K_UP]: 
                                self.y -= 3
                                self.up = True
                        if pressed[pg.K_DOWN]: 
                                self.y += 3
                                self.down = True
                        if pressed[pg.K_LEFT]: 
                                self.x -= 3
                                self.left = True
                        if pressed[pg.K_RIGHT]: 
                                self.x += 3
                                self.right = True
                        if math.sqrt((self.target[0] - self.x)**2 + (self.target[1] - self.y)**2) < 40:
                                self.points += 1
                                self.target = [randint(0,800), randint(0,600)]
        
        def start_game(self):
                if self.state == 0:
                        self.state = 1     
                        self.points = 0
                        self.x = 100
                        self.y = 100
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
        if game.state == 0:
                pygame.draw.rect(screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
                screen.blit(myfont.render("MENU", 1, (255,255,255)), (400, 300))
        elif game.state == 1:
                screen.fill((0,10,20))
                #pygame.draw.rect(screen, (10,123,50), pygame.Rect(game.x, game.y, 50, 50))
                if game.up:
                    sprite = game.sprites[4+int(pygame.time.get_ticks()/200)%2]
                elif game.down:
                    sprite = game.sprites[6+int(pygame.time.get_ticks()/200)%2]
                elif game.right:
                    sprite = game.sprites[8+int(pygame.time.get_ticks()/200)%2]
                elif game.left:
                    sprite = game.sprites[10+int(pygame.time.get_ticks()/200)%2]
                else:
                    sprite = game.sprites[int(pygame.time.get_ticks()/300)%2]
                sprite = pygame.transform.scale(sprite,(100,100))
                screen.blit(sprite, (game.x, game.y))
                pygame.draw.rect(screen, (123,50,10), pygame.Rect(game.target[0], game.target[1], 50, 50))
                screen.blit(myfont.render("Points: {}".format(game.points), 1, (255,255,0)), (100, 100))
        elif game.state == 2:
                pygame.draw.rect(screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
                screen.blit(myfont.render("PAUSE", 1, (255,255,255)), (400, 300))

pygame.init()
screen = pygame.display.set_mode((800, 600))
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

done = False

game = Game()

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        game.toggle_pause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        if game.started():
                                game.end_game()
                        else:
                                game.start_game()
        
        pressed = pygame.key.get_pressed()
        
        game.tick(pygame, pressed)
        draw_game()
        
        pygame.display.flip()
        clock.tick(60)

