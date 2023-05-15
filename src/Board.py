from math import floor
import pygame as p

from initialize_board import initialize_board
from image_arrays import game_pieces
from config import *

class Board:
  def __init__(self, game_window):
    self.game_window = game_window

    self.game_board = [
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None]
    ]
    initialize_board(game_window, self.game_board)

  def toggle_clicked_tile(self, clicked_position):

    # calculating which tile was clicked
    array_index_x = floor(clicked_position[0] / TILE_SIZE)
    array_index_y = floor(clicked_position[1] / TILE_SIZE)

    # tiles with no pieces should not be highlighted
    if (self.game_board[array_index_y][array_index_x].piece != None):

      # highlighting/unhighlighting the clicked tile
      if (self.game_board[array_index_y][array_index_x].is_clicked):
        self.game_board[array_index_y][array_index_x].is_clicked = False
        p.draw.rect(self.game_window, self.game_board[array_index_y][array_index_x].colour, self.game_board[array_index_y][array_index_x])
        self.game_window.blit(game_pieces[array_index_y][array_index_x].image.convert_alpha(), (array_index_x * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER, array_index_y * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER))

        # getting the clicked piece and displaying its move set
        piece = game_pieces[array_index_y][array_index_x]
        toggle_move_set(piece, game_pieces)

        p.display.update()
      else:
        self.game_board[array_index_y][array_index_x].is_clicked = True
        p.draw.rect(self.game_window, TILE_ORIGIN, self.game_board[array_index_y][array_index_x])
        self.game_window.blit(game_pieces[array_index_y][array_index_x].image.convert_alpha(), (array_index_x * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER, array_index_y * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER))
        p.display.update()

        piece = game_pieces[array_index_y][array_index_x]
        toggle_move_set(piece, game_pieces)

def toggle_move_set(piece, game_pieces):
  pass
  # print(piece.x, piece.y)