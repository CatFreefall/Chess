from pieces.Piece import Piece

class Pawn(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    # self.initial_pos = True