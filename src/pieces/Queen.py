from Piece import Piece

class Queen(Piece):
  def __init__(self, piece, colour, position):
    super().__init__(piece, colour, position)
    
    self.move_set = ["up", "up_right", "right", "down_right", "down", "down_left", "left", "up_left"]