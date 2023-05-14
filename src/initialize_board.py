import pygame as p

from config import TILE_SIZE, WINDOW_BORDER, PIECE_BORDER
from image_arrays import game_board, game_pieces

def initialize_board (game_window):
  game_window.fill(p.Color("white"))

  for i in range(0, len(game_board)):
    for j in range(0, len(game_board[i])):

      # generating tiles including the ones with coordinates
      tileCoordX = i * TILE_SIZE + WINDOW_BORDER
      tileCoordY = j * TILE_SIZE + WINDOW_BORDER
      game_window.blit(game_board[j][i].get_loaded_tile().convert(), (tileCoordX, tileCoordY))

      # generating pieces
      if (game_pieces[j][i] != "________"):
        pieceCoordX = tileCoordX + PIECE_BORDER
        pieceCoordY = tileCoordY + PIECE_BORDER
        game_window.blit(game_pieces[j][i].convert_alpha(), (pieceCoordX, pieceCoordY))