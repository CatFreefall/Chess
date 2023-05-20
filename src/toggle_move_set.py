import pygame as p

from config import *
from get_clicked_tile import get_clicked_tile


def hide_move_set(game_window, game_board, clicked_position):
  clicked_tile = get_clicked_tile(clicked_position)

  # tiles with no pieces should not be highlighted
  if (game_board[clicked_tile[1]][clicked_tile[0]].piece != None):

    # if tile is already clicked, clicking it again should unhighlight it
    if (game_board[clicked_tile[1]][clicked_tile[0]].is_clicked):
      game_board[clicked_tile[1]][clicked_tile[0]].is_clicked = False

      # redrawing the tile and piece over the tile
      tile_colour = game_board[clicked_tile[1]][clicked_tile[0]].colour
      draw_tile(game_window, game_board, tile_colour, clicked_tile)
      draw_piece(game_window, game_board, clicked_tile)

      # unhighlighting the clicked piece's move set and updating the window
      get_move_set(game_window, game_board, clicked_tile[0], clicked_tile[1])
      p.display.update()

def show_move_set(game_window, game_board, clicked_position):
  clicked_tile = get_clicked_tile(clicked_position)

  if (game_board[clicked_tile[1]][clicked_tile[0]].piece != None):
    game_board[clicked_tile[1]][clicked_tile[0]].is_clicked = True

    draw_tile(game_window, game_board, TILE_ORIGIN, clicked_tile)
    draw_piece(game_window, game_board, clicked_tile)

    move_set = get_move_set(game_window, game_board, clicked_tile[0], clicked_tile[1])
    p.display.update()

    return move_set


# helper functions
def draw_tile(game_window, game_board, tile_colour, clicked_tile):
  tile = game_board[clicked_tile[1]][clicked_tile[0]]
  p.draw.rect(game_window, tile_colour, tile)

def draw_piece(game_window, game_board, clicked_tile):
  piece = game_board[clicked_tile[1]][clicked_tile[0]].piece.image.convert_alpha()
  pieceCoordX = clicked_tile[0] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  pieceCoordY = clicked_tile[1] * TILE_SIZE + WINDOW_BORDER + PIECE_BORDER
  game_window.blit(piece, (pieceCoordX, pieceCoordY))

# TODO: note that for pawns, initial_position needs to be toggled to False after the first move
def get_move_set(game_window, game_board, array_index_x, array_index_y):
  if (game_board[array_index_y][array_index_x].is_clicked):

    # holds all possible moves and captures for the selected piece
    move_set = {
      "clicked_index": [array_index_x, array_index_y],
      "move": [],
      "capture": []
    }

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

              # pawn's do not capture vertically.
              if (game_board[array_index_y][array_index_x].piece.piece_type == "pawn"):
                if (j == "up" or j == "down"):
                  break

              draw_tile(game_window, game_board, TILE_CAPTURE, [current_index_x, current_index_y])
              draw_piece(game_window, game_board, [current_index_x, current_index_y])

              # adding the tile to the move set to be returned
              move_set["capture"].append(game_board[current_index_y][current_index_x])

              break
            else:
              break
          else:
            
            # pawn's cannot move vertically unless capturing
            if (game_board[array_index_y][array_index_x].piece.piece_type == "pawn"):
              if (j == "up_left" or j == "up_right" or j == "down_left" or j == "down_right"):
                break

            draw_tile(game_window, game_board, TILE_DESTINATION, [current_index_x, current_index_y])

            # adding the tile to the move set to be returned
            move_set["move"].append(game_board[current_index_y][current_index_x])

        else:
          break

    # returning the move set of clicked piece. 
    # unclicking a piece will not return a move set.
    return move_set

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
              
              if (game_board[array_index_y][array_index_x].piece.piece_type == "pawn"):
                if (j == "up" or j == "down"):
                  break

              tile_colour = game_board[current_index_y][current_index_x].colour
              draw_tile(game_window, game_board, tile_colour, [current_index_x, current_index_y])
              draw_piece(game_window, game_board, [current_index_x, current_index_y])
              break
            else:
              break
          else:
            
            if (game_board[array_index_y][array_index_x].piece.piece_type == "pawn"):
              if (j == "up_left" or j == "up_right" or j == "down_left" or j == "down_right"):
                break

            tile_colour = game_board[current_index_y][current_index_x].colour
            draw_tile(game_window, game_board, tile_colour, [current_index_x, current_index_y])
        else:
          break


# helper function for get_move_set
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