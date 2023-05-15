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
    clicked_tile = get_clicked_tile(clicked_position)

    # tiles with no pieces should not be highlighted
    if (self.game_board[clicked_tile[1]][clicked_tile[0]].piece != None):

      # highlighting/unhighlighting the clicked tile
      if (self.game_board[clicked_tile[1]][clicked_tile[0]].is_clicked):
        self.game_board[clicked_tile[1]][clicked_tile[0]].is_clicked = False
        p.draw.rect(self.game_window, self.game_board[clicked_tile[1]][clicked_tile[0]].colour, self.game_board[clicked_tile[1]][clicked_tile[0]])
        self.game_window.blit(game_pieces[clicked_tile[1]][clicked_tile[0]].image.convert_alpha(), (clicked_tile[0] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER, clicked_tile[1] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER))

        # displaying the clicked pieces move set
        toggle_move_set(self.game_window, self.game_board, clicked_tile[0], clicked_tile[1])
        p.display.update()

      else:
        self.game_board[clicked_tile[1]][clicked_tile[0]].is_clicked = True
        p.draw.rect(self.game_window, TILE_ORIGIN, self.game_board[clicked_tile[1]][clicked_tile[0]])
        self.game_window.blit(game_pieces[clicked_tile[1]][clicked_tile[0]].image.convert_alpha(), (clicked_tile[0] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER, clicked_tile[1] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER))

        toggle_move_set(self.game_window, self.game_board, clicked_tile[0], clicked_tile[1])
        p.display.update()
        # TODO: note that for pawns, initial_position needs to be toggled to False after the first move

# helper functions
def toggle_move_set(game_window, game_board, array_index_x, array_index_y):
  pass

def get_clicked_tile(clicked_position):
  return [floor(clicked_position[0] / TILE_SIZE), floor(clicked_position[1] / TILE_SIZE)]
