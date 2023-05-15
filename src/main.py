import pygame as p

from config import WINDOW_SIZE
from Board import Board

current_game = None

p.init()
p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)

game_window = p.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

current_game = Board(game_window)
p.display.update()

while True:

  event = p.event.wait()
  if event.type == p.QUIT:
    p.quit()
    quit()

  elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
    current_game.change_clicked_tile(p.mouse.get_pos())

  else:
    continue
