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

      # if tile is already clicked, clicking it again should unhighlight it
      if (self.game_board[clicked_tile[1]][clicked_tile[0]].is_clicked):
        self.game_board[clicked_tile[1]][clicked_tile[0]].is_clicked = False

        # redrawing the tile
        tile_colour = self.game_board[clicked_tile[1]][clicked_tile[0]].colour
        draw_tile(self.game_window, self.game_board, tile_colour, clicked_tile)

        # redrawing the piece over the tile
        draw_piece(self.game_window, game_pieces, clicked_tile)

        # unhighlighting the clicked piece's move set and updating the window
        toggle_move_set(self.game_window, self.game_board, clicked_tile[0], clicked_tile[1])
        p.display.update()

      # if tile is not clicked, clicking it should highlight it
      else:
        self.game_board[clicked_tile[1]][clicked_tile[0]].is_clicked = True

        # redrawing the tile
        draw_tile(self.game_window, self.game_board, TILE_ORIGIN, clicked_tile)

        # redrawing the piece over the tile
        draw_piece(self.game_window, game_pieces, clicked_tile)

        # displaying the clicked piece's move set and updating the window
        toggle_move_set(self.game_window, self.game_board, clicked_tile[0], clicked_tile[1])
        p.display.update()

# helper functions
def draw_tile(game_window, game_board, tile_colour, clicked_tile):
  tile = game_board[clicked_tile[1]][clicked_tile[0]]
  p.draw.rect(game_window, tile_colour, tile)

def draw_piece(game_window, game_pieces, clicked_tile):
  piece = game_pieces[clicked_tile[1]][clicked_tile[0]].image.convert_alpha()
  pieceCoordX = clicked_tile[0] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  pieceCoordY = clicked_tile[1] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  game_window.blit(piece, (pieceCoordX, pieceCoordY))

# TODO: note that for pawns, initial_position needs to be toggled to False after the first move
def toggle_move_set(game_window, game_board, array_index_x, array_index_y):
  if (game_board[array_index_y][array_index_x].is_clicked):
    print("clicked")
  else:
    print("unclicked")
  print(game_board[array_index_y][array_index_x].piece.move_set)

def get_clicked_tile(clicked_position):
  return [floor(clicked_position[0] / TILE_SIZE), floor(clicked_position[1] / TILE_SIZE)]