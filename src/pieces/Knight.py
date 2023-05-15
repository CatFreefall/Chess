# TODO: Add unique move_set for knight

from pieces.Piece import Piece

class Knight(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)

    self.move_set = {
      "up_up_left": [1],
      "up_left_left": [1],
      "down_left_left": [1],
      "down_down_left": [1],
      "down_down_right": [1],
      "down_right_right": [1],
      "up_right_right": [1],
      "up_up_right": [1]
    }