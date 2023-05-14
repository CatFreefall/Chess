class Tile:
  def __init__(self, loaded_tile):
    self.is_occupied = False
    self.loaded_tile = loaded_tile

  def get_loaded_tile(self):
    return self.loaded_tile

  def set_occupied(self):
    self.is_occupied = True
  
  def set_unoccupied(self):
    self.is_occupied = False

  def is_occupied(self):
    return self.is_occupied