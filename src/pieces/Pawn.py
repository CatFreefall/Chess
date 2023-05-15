from Piece import Piece

class Pawn(Piece):
  def __init__(self, piece, colour, position):
    super().__init__(piece, colour, position)

    self.initial_pos = True
    
    if (colour == "white"):
      self.move_set = ["up"]
    else:
      self.move_set = ["down"]