import pygame
from sys import exit
import player as popcorn_player
import pop as popcorn_pop
import mixer as popcorn_mixer
from asyncio import sleep

class Game():
    
    def __init__(self, title, x, y):
        super().__init__()
        pygame.init()
        pygame.font.init()
        
        self.playing = False
        
        self.running = True
        self.TITLE = title
        self.x = x
        self.y = y
        self.FPS = 60
        
        self.amount = 5
        self.score = 0
        self.best_score = 0
        self.heart = 8
        self.height = 8
        
        self.velocity = 0.25
        
        #Window
        self.screen = pygame.display.set_mode((self.x , self.y))
        pygame.display.set_caption(self.TITLE)
        pygame.display.set_icon(pygame.image.load('./assets/img/bucket.png'))
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('./assets/fonts/popcorn_font.ttf', 40)
        
        #Player
        self.player = popcorn_player.Player(self.screen)
        
        #Pop
        self.all_pops = pygame.sprite.Group()
        
        #Mixer
        self.mixer = popcorn_mixer.Mixer()
    
    def spawn_pops(self):
        pop = popcorn_pop.POP(self.screen, self.velocity)
        self.all_pops.add(pop)
    
    #Utiles
    
    TEXT_COL = (255, 255, 255)
    
    def draw_text(self, text, font, text_col, x, y, opacity):
        img = self.font.render(text, True, text_col)
        img.set_alpha(opacity)
        self.screen.blit(img, (x, y))
    
    dead_zone = pygame.Surface((700, 25))
    dead_zone_rect = dead_zone.get_rect(topleft=(0, 675))
    def update(self):
        
        ##POPS
        for pop in self.all_pops:
                if self.player.rect.colliderect(pop.rect):
                    
                    self.score += 1
                    pop.kill()
                    self.mixer.play_sound('./assets/audio/pop.mp3')
                    self.spawn_pops()
                    for i in range(40):
                        if not i == 0:
                            if self.score == i*25:
                                self.velocity += 0.5
                                break
                    
                if self.dead_zone_rect.colliderect(pop.rect):
                    self.height -= 1
                    
                    if self.height == 0:
                        if self.score > self.best_score:
                            self.best_score = self.score
                            self.all_pops.empty()
                        self.playing = False
                        self.score = 0
                        self.velocity = 0.25
                        self.height = 8
                        self.player.change_size(self.height)
                        self.mixer.play_sound('./assets/audio/game_over.mp3')
                        break
                    
                    pop.kill()
                    self.player.change_size(self.height)
                    self.mixer.play_sound('./assets/audio/lost_pop.mp3')
                    self.spawn_pops()
        
        ##MOVEMENTS
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(way='left')
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(way='right')
        
        ##DRAW
        self.screen.fill((255, 57, 45))
        
        #Dead zone
        
        self.dead_zone.fill(pygame.Color("black"))
        self.screen.blit(self.dead_zone, (0, 675))
        
        self.draw_text(text='Score : ' + str(self.score), font=self.font, text_col=self.TEXT_COL, x=5, y=12.5, opacity=200)
        
        self.all_pops.update()
        self.player.update()
        pygame.display.flip()
        pygame.display.update()
    
    ## MENU CONTENT
    menu_image = pygame.image.load('./assets/img/menu.png') 
    play_button = pygame.image.load('./assets/img/play_button.png')
    play_button = pygame.transform.scale2x(play_button)
    play_button_rect = play_button.get_rect(topleft=(250, 350))
    
    def tick_menu(self):
        self.screen.blit(self.menu_image, (0, 0))
        self.screen.blit(self.play_button, (250, 350))
        self.draw_text(text='Best Score : ' + str(self.best_score), font=self.font, text_col=self.TEXT_COL, x=250, y=250, opacity=200)
        pygame.display.flip()
        pygame.display.update()
    
    async def run(self):
        self.clock.tick(self.FPS)
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos) and not self.playing:
                        self.playing = True
                        for i in range(self.amount):
                            self.spawn_pops()
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit()
            if self.playing:
                self.update()
            else:
                self.tick_menu()
        await sleep(0)