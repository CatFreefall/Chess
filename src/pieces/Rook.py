from pieces.Piece import Piece

class Rook(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    self.move_set = [
      ["up", "up", "up", "up", "up", "up", "up"],
      ["left", "left", "left", "left", "left", "left", "left"],
      ["down", "down", "down", "down", "down", "down", "down"],
      ["right", "right", "right", "right", "right", "right", "right"]
    ]