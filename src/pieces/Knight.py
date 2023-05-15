# TODO: Add unique move_set for knight

from pieces.Piece import Piece

class Knight(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)

    # move_set = ["up_up_left", "up_up_right", "up_right_right", "down_right_right", "down_down_right", "down_down_left", "down_left_left", "up_left_left"]