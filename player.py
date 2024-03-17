import pygame

POSITION = {
    'total_left': 0,
    'center': 300,
    'total_right': 600
}

class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        super().__init__()
        pygame.init()
        
        self.size = 8
        
        self.screen = screen
        self.image = pygame.image.load('./assets/img/bucket.png')
        self.image = pygame.transform.scale(self.image, (100, 100 + self.size * 10))
        self.rect = self.image.get_rect(center=(POSITION['center'], self.screen.get_height() - 100))
        
        self.x = self.rect.x
        self.x = 300
        self.height = self.screen.get_height() - 195
        
        self.velocity = 1
        
        self.pos = 4
    
    def move_left(self): self.x -= self.velocity
    def move_right(self): self.x += self.velocity
    
    def change_size(self, size):
        self.size = size
        self.image = pygame.transform.scale(self.image, (100, 100 + self.size * 10))
        self.height = self.screen.get_height() - int(100 + size*10 + 25)
    
    def move(self, way):
        if way == 'left':
            if not self.x == POSITION['total_left']:
                self.pos -= 1
                self.move_left()
        elif way == 'right':
            if not self.x == POSITION['total_right']:
                self.pos += 1
                self.move_right()
        
    def update(self): 
        self.screen.blit(self.image, (self.x, self.height))
        self.rect = self.image.get_rect(center=(self.x, self.height))