import pygame as pg
import sys
import os
import sys

from src.game import Game

# Get the parent directory of the directory containing 'src'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the Python path
sys.path.append(project_root)

# Now import the 'src' module
from src.game import Game

pg.init()
pg.mixer.init()
pg.font.init()

WIDTH = 1280
HEIGHT = 720
window_size = pg.Vector2(WIDTH, HEIGHT)

screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()

pg.display.set_caption("Risk")

game = Game(screen, clock, window_size)
game.run()

pg.quit()
sys.exit()
