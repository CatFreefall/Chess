from pieces.Piece import Piece

class Bishop(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = {
      "up_left": [1, 2, 3, 4, 5, 6, 7],
      "down_left": [1, 2, 3, 4, 5, 6, 7],
      "down_right": [1, 2, 3, 4, 5, 6, 7],
      "up_right": [1, 2, 3, 4, 5, 6, 7]
    }