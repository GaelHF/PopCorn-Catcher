import os
os.system('pip install pygame')

import pygame
from sys import exit
import game

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    popcorn = game.Game('POPCORN CATCH', 700, 700)
    popcorn.run()
exit()