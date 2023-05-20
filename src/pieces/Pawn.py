from pieces.Piece import Piece

class Pawn(Piece):
  def __init__(self, piece_type, colour, loaded_image):
    Piece.__init__(self, piece_type, colour, loaded_image)

    match self.colour:
      case "white":
        self.move_set = [
          ["up", "up"],
          ["up_left"],
          ["up_right"]
        ]
      
      case "black":
        self.move_set = [
          ["down", "down"],
          ["down_right"],
          ["down_left"]
        ]

  def change_move_set(self):
    match self.colour:
      case "white":
      
        self.move_set = [
          ["up"],
          ["up_left"],
          ["up_right"]
        ]
      
      case "black":
      
        self.move_set = [
          ["down"],
          ["down_right"],
          ["down_left"]
        ]