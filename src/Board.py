from initialize_board import initialize_board

class Board:
  def __init__(self, game_window):
    initialize_board(game_window)

  def move_piece(self, piece, new_pos):
    piece.move(new_pos)