import pygame as p

from initialize_board import initialize_board
from image_arrays import game_pieces
from config import *
from get_clicked_tile import get_clicked_tile

class DrawMoves:
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

        # redrawing the tile and piece over the tile
        tile_colour = self.game_board[clicked_tile[1]][clicked_tile[0]].colour
        draw_tile(self.game_window, self.game_board, tile_colour, clicked_tile)
        draw_piece(self.game_window, game_pieces, clicked_tile)

        # unhighlighting the clicked piece's move set and updating the window
        toggle_move_set(self.game_window, self.game_board, clicked_tile[0], clicked_tile[1])
        p.display.update()

      # if tile is not clicked, clicking it should highlight it
      else:
        self.game_board[clicked_tile[1]][clicked_tile[0]].is_clicked = True

        # redrawing the tile and piece over the tile
        draw_tile(self.game_window, self.game_board, TILE_ORIGIN, clicked_tile)
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
# TODO: pawns capture diagonally, but they move forward vertically
def toggle_move_set(game_window, game_board, array_index_x, array_index_y):
  if (game_board[array_index_y][array_index_x].is_clicked):

    # iterating through all directions in the piece's move set
    for i in game_board[array_index_y][array_index_x].piece.move_set:
      
      current_index_x = array_index_x
      current_index_y = array_index_y

      # iterating through the length of the piece's current move set
      for j in i:
        current_move_set = get_move_tile_index(j, current_index_x, current_index_y)
        current_index_x = current_move_set[0]
        current_index_y = current_move_set[1]

        # break to next direction if piece is out of bounds
        # use a different tile colour if selected piece can capture another piece
        # draw tile path if not out of bounds and if no piece is in the way
        if (0 <= current_index_x <= 7 and 0 <= current_index_y <= 7):
          if (game_board[current_index_y][current_index_x].piece != None):
            if (game_board[current_index_y][current_index_x].piece.colour != game_board[array_index_y][array_index_x].piece.colour):
              draw_tile(game_window, game_board, TILE_CAPTURE, [current_index_x, current_index_y])
              draw_piece(game_window, game_pieces, [current_index_x, current_index_y])
              break
            else:
              break
          else:
            draw_tile(game_window, game_board, TILE_DESTINATION, [current_index_x, current_index_y])
        else:
          break

  else:
    for i in game_board[array_index_y][array_index_x].piece.move_set:
      
      current_index_x = array_index_x
      current_index_y = array_index_y

      for j in i:
        current_move_set = get_move_tile_index(j, current_index_x, current_index_y)

        current_index_x = current_move_set[0]
        current_index_y = current_move_set[1]

        if (0 <= current_index_x <= 7 and 0 <= current_index_y <= 7):
          if (game_board[current_index_y][current_index_x].piece != None):
            if (game_board[current_index_y][current_index_x].piece.colour != game_board[array_index_y][array_index_x].piece.colour):
              
              tile_colour = game_board[current_index_y][current_index_x].colour
              draw_tile(game_window, game_board, tile_colour, [current_index_x, current_index_y])
              draw_piece(game_window, game_pieces, [current_index_x, current_index_y])
              break
            else:
              break
          else:
            tile_colour = game_board[current_index_y][current_index_x].colour
            draw_tile(game_window, game_board, tile_colour, [current_index_x, current_index_y])
        else:
          break


# helper function for toggle_move_set
def get_move_tile_index(current_move, current_index_x, current_index_y):
  current_move_set = current_move.split("_")

  for k in current_move_set:
    match k:
      case "up":
        current_index_y = current_index_y - 1
      case "left":
        current_index_x = current_index_x + 1
      case "down":
        current_index_y = current_index_y + 1
      case "right":
        current_index_x = current_index_x - 1

  return [current_index_x, current_index_y]