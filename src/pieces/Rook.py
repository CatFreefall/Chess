from pieces.Piece import Piece

class Rook(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = {
      "top": [1, 2, 3, 4, 5, 6, 7],
      "left": [1, 2, 3, 4, 5, 6, 7],
      "bottom": [1, 2, 3, 4, 5, 6, 7],
      "right": [1, 2, 3, 4, 5, 6, 7]
    }