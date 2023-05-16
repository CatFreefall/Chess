from pieces.Piece import Piece

class Pawn(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    self.initial_pos = True

    match self.initial_pos:
      case True:
        if (self.colour == "white"):
          self.move_set = [
            ["up", "up"]
          ]
        
        else:
          self.move_set = [
            ["down", "down"]
          ]
      
      case False:
        if (self.colour == "white"):
          self.move_set = [
            ["up"]
          ]
        
        else:
          self.move_set = [
            ["down"]
          ]