from initialize_board import initialize_board

class Board:
  def __init__(self, game_window):
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

  def move_piece(self, piece, new_pos):
    piece.move(new_pos)