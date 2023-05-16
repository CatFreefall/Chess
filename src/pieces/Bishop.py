from pieces.Piece import Piece

class Bishop(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = [
      ["up_left", "up_left", "up_left", "up_left", "up_left", "up_left", "up_left"],
      ["down_left", "down_left", "down_left", "down_left", "down_left", "down_left", "down_left"],
      ["down_right", "down_right", "down_right", "down_right", "down_right", "down_right", "down_right"],
      ["up_right", "up_right", "up_right", "up_right", "up_right", "up_right", "up_right"]
    ]