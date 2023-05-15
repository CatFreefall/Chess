import pygame as p

from config import WINDOW_SIZE
from Board import Board, get_clicked_tile

current_tile_pos = None
previous_tile_pos = None

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
    
    previous_tile_pos = current_tile_pos
    current_tile_pos = p.mouse.get_pos()

    # tile clicked is previous tile, in this case, unclick it
    if (previous_tile_pos != None and get_clicked_tile(current_tile_pos) == get_clicked_tile(previous_tile_pos)):
      current_game.toggle_clicked_tile(current_tile_pos)
      current_tile_pos = None
      continue

    # tile clicked is not previous tile, in this clase, unclick previous tile
    elif (previous_tile_pos != None):
      current_game.toggle_clicked_tile(previous_tile_pos)

    # click current tile
    current_game.toggle_clicked_tile(current_tile_pos)

  else:
    continue