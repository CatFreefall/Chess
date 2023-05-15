from Piece import Piece

class Rook(Piece):
  def __init__(self, piece, colour, position):
    super().__init__(piece, colour, position)
    
    self.move_set = ["up_right", "down_right", "down_left", "up_left"]