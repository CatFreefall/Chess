from pieces.Piece import Piece

class King(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = [
      ["up"],
      ["up_left"],
      ["left"],
      ["down_left"],
      ["down"],
      ["down_right"],
      ["right"],
      ["up_right"]
    ]