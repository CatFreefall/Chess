from pieces.Piece import Piece

class Rook(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = ["up", "down", "left", "right"]