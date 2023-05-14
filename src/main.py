import pygame as p

from config import WINDOW_WIDTH, WINDOW_HEIGHT
from Board import Board

p.init()

game_window = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
  for event in p.event.get():
    if event.type == p.QUIT:
      p.quit()
      quit()
    else:
      Board(game_window)
      p.display.update()
