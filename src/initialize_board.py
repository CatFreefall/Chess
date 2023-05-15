import pygame as p

from config import TILE_SIZE, WINDOW_BORDER, PIECE_BORDER, TILE_BORDER
from image_arrays import game_tiles, game_pieces
from Tile import Tile

def initialize_board (game_window, game_board):
  game_window.fill(p.Color("white"))

  for i in range(0, len(game_board)):
    for j in range(0, len(game_board[i])):

      # generating tiles
      tileCoordX = i * TILE_SIZE + WINDOW_BORDER
      tileCoordY = j * TILE_SIZE + WINDOW_BORDER

      game_board[j][i] = Tile((tileCoordX, tileCoordY, TILE_SIZE - TILE_BORDER, TILE_SIZE - TILE_BORDER), game_tiles[j][i])
      p.draw.rect(game_window, (game_board[j][i].colour), game_board[j][i])

      # generating pieces
      if (game_pieces[j][i] != "________"):
        pieceCoordX = tileCoordX + PIECE_BORDER
        pieceCoordY = tileCoordY + PIECE_BORDER

        game_board[j][i].is_occupied = True

        game_window.blit(game_pieces[j][i].convert_alpha(), (pieceCoordX, pieceCoordY))