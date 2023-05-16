from math import floor

from config import TILE_SIZE

def get_clicked_tile(clicked_position):
  return [floor(clicked_position[0] / TILE_SIZE), floor(clicked_position[1] / TILE_SIZE)]