import pygame as p

from config import WINDOW_SIZE
from toggle_move_set import show_move_set, hide_move_set, draw_tile
from get_clicked_tile import get_clicked_tile
from GameBoard import GameBoard
from initialize_board import initialize_board
from config import *

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
        print("This is a valid move")
      continue

    elif (current_piece.colour != tile_turn):
      if (current_move_set != None and board.game_board[current_tile[1]][current_tile[0]] in current_move_set.get("capture")):
        print("This is a valid capture")
        hide_move_set(game_window, board.game_board, previous_tile_pos)
        
        previous_tile = get_clicked_tile(previous_tile_pos)
        board.game_board[current_tile[1]][current_tile[0]].piece = board.game_board[previous_tile[1]][previous_tile[0]].piece
        piece = board.game_board[previous_tile[1]][previous_tile[0]].piece.image.convert_alpha()
        board.game_board[previous_tile[1]][previous_tile[0]].piece = None
        print(board.game_board[current_tile[1]][current_tile[0]].colour)
        p.draw.rect(game_window, board.game_board[previous_tile[1]][previous_tile[0]].colour, board.game_board[previous_tile[1]][previous_tile[0]])
        pieceCoordX = current_tile[0] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
        pieceCoordY = current_tile[1] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
        p.draw.rect(game_window, board.game_board[current_tile[1]][current_tile[0]].colour, board.game_board[current_tile[1]][current_tile[0]])
        game_window.blit(piece, (pieceCoordX, pieceCoordY))
        p.display.update()

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