from pieces.Piece import Piece

class King(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = {
      "up": [1],
      "up_left": [1],
      "left": [1],
      "down_left": [1],
      "down": [1],
      "down_right": [1],
      "right": [1],
      "up_right": [1]
    }