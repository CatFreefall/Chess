from pieces.Piece import Piece

class Pawn(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    self.initial_pos = True

    match self.initial_pos:
      case True:
        if (self.colour == "white"):
          self.move_set = {
            "up": [1, 2]
          }
        
        else:
          self.move_set = {
            "down": [1, 2]
          }
      
      case False:
        if (self.colour == "white"):
          self.move_set = {
            "up": [1],
          }
        
        else:
          self.move_set = {
            "down": [1],
          }