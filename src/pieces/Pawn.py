from pieces.Piece import Piece

class Pawn(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)
    self.initial_pos = True

    match self.colour:
      case "white":
        if (self.initial_pos == True):
          self.move_set = [
            ["up", "up"],
            ["up_left"],
            ["up_right"]
          ]
        
        else:
          self.move_set = [
            ["up"],
            ["up_left"],
            ["up_right"]
          ]
      
      case "black":
        if (self.initial_pos == True):
          self.move_set = [
            ["down", "down"],
            ["down_right"],
            ["down_left"]
          ]
        
        else:
          self.move_set = [
            ["down"],
            ["down_right"],
            ["down_left"]
          ]