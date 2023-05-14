class pawn:
    def __init__(self, colour, position):
      self.piece = pawn
      self.colour = colour
      self.name = colour.upper() + "_PAWN"

      self.position = position
      self.initial_pos = True

        
    def move(self, new_pos):
      self.position = new_pos
      self.initial_pos = False

    def get_name(self):
      return self.name