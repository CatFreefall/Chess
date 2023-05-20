import pygame as p

from config import WINDOW_SIZE, TILE_SIZE, WINDOW_BORDER, PIECE_BORDER
from toggle_move_set import show_move_set, hide_move_set
from get_clicked_tile import get_clicked_tile
from GameBoard import GameBoard
from initialize_board import initialize_board
from move_and_capture import move_and_capture

tile_turn = "white"

current_tile_pos = None
previous_tile_pos = None
current_move_set = None

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
    
    current_tile_pos = p.mouse.get_pos()
    current_tile = get_clicked_tile(current_tile_pos)

    current_piece = board.game_board[current_tile[1]][current_tile[0]].piece

    if (current_piece != None and current_piece.colour == tile_turn and previous_tile_pos == None):
      current_move_set = show_move_set(game_window, board.game_board, current_tile_pos)
      previous_tile_pos = current_tile_pos

    elif (current_piece == None):
      print("Just an ordinary tile")
      if (current_move_set != None and board.game_board[current_tile[1]][current_tile[0]] in current_move_set.get("move")):
        move_and_capture(game_window, board.game_board, current_tile, previous_tile_pos)

        if (board.game_board[current_tile[1]][current_tile[0]].piece.piece_type == "pawn"):
          # print("OOGA OOGA YES")
          print(board.game_board[1][2] == board.game_board[1][3])
          board.game_board[current_tile[1]][current_tile[0]].piece.change_move_set()
          #TODO: change move set of a pawn after it moves once

        if (tile_turn == "white"):
          tile_turn = "black"
        else:
          tile_turn = "white"

        current_tile_pos = None
        previous_tile_pos = None
        current_move_set = None
      continue

    elif (current_piece.colour != tile_turn):
      if (current_move_set != None and board.game_board[current_tile[1]][current_tile[0]] in current_move_set.get("capture")):
        move_and_capture(game_window, board.game_board, current_tile, previous_tile_pos)

        if (tile_turn == "white"):
          tile_turn = "black"
        else:
          tile_turn = "white"

        current_tile_pos = None
        previous_tile_pos = None
        current_move_set = None

      continue

    elif (current_tile == get_clicked_tile(previous_tile_pos)):
      hide_move_set(game_window, board.game_board, current_tile_pos)
      current_tile_pos = None
      previous_tile_pos = None
      current_move_set = None
      continue

  else:
    continue