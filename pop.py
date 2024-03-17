import pygame
from player import POSITION
from random import randint

class POP(pygame.sprite.Sprite):
    
    def __init__(self, screen, velocity):
        super().__init__()
        pygame.init()
        
        self.screen = screen
        
        self.image = pygame.image.load(f'./assets/img/pop{str(randint(1,3))}.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.start_pos = randint(POSITION['total_left'], POSITION['total_right'])
        
        self.rect = self.image.get_rect(center=(self.start_pos, 0))
        
        self.x = self.rect.x
        self.x = self.start_pos
        
        self.y = self.rect.y
        self.y = 0
    
        self.velocity = velocity
        
    def fall(self): self.y += self.velocity
    
    
    def update(self): 
        self.screen.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.fall()