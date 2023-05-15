from pieces.Piece import Piece

class King(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    
    # self.move_set = ["up", "up_right", "right", "down_right", "down", "down_left", "left", "up_left"]