import pygame

class Mixer():
    
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
    
    def play_sound(self, sound):
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
    
    def stop_sound(self):
        pygame.mixer.music.stop()