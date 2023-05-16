from pieces.Piece import Piece

class Queen(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = [
      ["up", "up", "up", "up", "up", "up", "up"],
      ["up_left", "up_left", "up_left", "up_left", "up_left", "up_left", "up_left"],
      ["left", "left", "left", "left", "left", "left", "left"],
      ["down_left", "down_left", "down_left", "down_left", "down_left", "down_left", "down_left"],
      ["down", "down", "down", "down", "down", "down", "down"],
      ["down_right", "down_right", "down_right", "down_right", "down_right", "down_right", "down_right"],
      ["right", "right", "right", "right", "right", "right", "right"],
      ["up_right", "up_right", "up_right", "up_right", "up_right", "up_right", "up_right"]
    ]