import pygame as p
from toggle_move_set import hide_move_set
from get_clicked_tile import get_clicked_tile
from config import WINDOW_BORDER, PIECE_BORDER, TILE_SIZE

def move_and_capture(game_window, game_board, current_tile, previous_tile_pos):
  hide_move_set(game_window, game_board, previous_tile_pos)
        
  previous_tile = get_clicked_tile(previous_tile_pos)
  game_board[current_tile[1]][current_tile[0]].piece = game_board[previous_tile[1]][previous_tile[0]].piece
  piece = game_board[previous_tile[1]][previous_tile[0]].piece.image.convert_alpha()
  game_board[previous_tile[1]][previous_tile[0]].piece = None
  p.draw.rect(game_window, game_board[previous_tile[1]][previous_tile[0]].colour, game_board[previous_tile[1]][previous_tile[0]])
  pieceCoordX = current_tile[0] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  pieceCoordY = current_tile[1] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  p.draw.rect(game_window, game_board[current_tile[1]][current_tile[0]].colour, game_board[current_tile[1]][current_tile[0]])
  game_window.blit(piece, (pieceCoordX, pieceCoordY))
  p.display.update()