import pygame as p

from config import WINDOW_SIZE
from GetMoves import show_move_set, hide_move_set
from get_clicked_tile import get_clicked_tile
from GameBoard import GameBoard
from initialize_board import initialize_board

current_tile_pos = None
previous_tile_pos = None

p.init()
p.mouse.set_cursor(p.SYSTEM_CURSOR_HAND)
p.display.set_caption("Chess")

game_window = p.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

board = GameBoard()
initialize_board(game_window, board.game_board)

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
      hide_move_set(game_window, board.game_board, current_tile_pos)
      current_tile_pos = None
      continue

    # tile clicked is not previous tile, in this clase, unclick previous tile
    elif (previous_tile_pos != None):
      hide_move_set(game_window, board.game_board, previous_tile_pos)

    # click new current tile
    current_move_set = show_move_set(game_window, board.game_board, current_tile_pos)
    #TODO: change board state based on current_move_set.
    #TODO: add player turns
    #TODO: also move if a tile in purple is selected instead of deselecting piece

  else:
    continue