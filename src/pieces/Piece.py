class Piece:
    def __init__(self, piece, colour, position):
      self.colour = colour
      self.name = colour.upper() + "_" + piece.upper()

      self.position = position

        
    def move(self, new_pos):
      self.position = new_pos
      self.initial_pos = False

    def get_name(self):
      return self.name