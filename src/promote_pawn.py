import pygame as p

from loaded_pieces import BLACK_QUEEN, WHITE_QUEEN, BLACK_ROOK, WHITE_ROOK, BLACK_KNIGHT, WHITE_KNIGHT, BLACK_BISHOP, WHITE_BISHOP
from config import *

def promote_pawn(game_window, game_board, current_tile, selected_promotion):
  match selected_promotion:
    case "Queen":
      if (game_board[current_tile[1]][current_tile[0]].piece.colour == "black"):
        game_board[current_tile[1]][current_tile[0]].piece = BLACK_QUEEN
      else:
        game_board[current_tile[1]][current_tile[0]].piece = WHITE_QUEEN
    case "Rook":
      if (game_board[current_tile[1]][current_tile[0]].piece.colour == "black"):
        game_board[current_tile[1]][current_tile[0]].piece = BLACK_ROOK
      else:
        game_board[current_tile[1]][current_tile[0]].piece = WHITE_ROOK
    case "Knight":
      if (game_board[current_tile[1]][current_tile[0]].piece.colour == "black"):
        game_board[current_tile[1]][current_tile[0]].piece = BLACK_KNIGHT
      else:
        game_board[current_tile[1]][current_tile[0]].piece = WHITE_KNIGHT
    case "Bishop":
      if (game_board[current_tile[1]][current_tile[0]].piece.colour == "black"):
        game_board[current_tile[1]][current_tile[0]].piece = BLACK_BISHOP
      else:
        game_board[current_tile[1]][current_tile[0]].piece = WHITE_BISHOP

  p.draw.rect(game_window, game_board[current_tile[1]][current_tile[0]].colour, game_board[current_tile[1]][current_tile[0]])
  pieceCoordX = current_tile[0] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  pieceCoordY = current_tile[1] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  piece = game_board[current_tile[1]][current_tile[0]].piece.image.convert_alpha()
  game_window.blit(piece, (pieceCoordX, pieceCoordY))
  p.display.update()
