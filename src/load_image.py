import pygame as p

from config import TILE_SIZE, PIECE_SIZE, TILE_BORDER

# This function loads an image from a file, increases its quality, and scales it to the tile size
def load_tile(location):
  return p.transform.smoothscale(p.image.load(location), (TILE_SIZE - TILE_BORDER, TILE_SIZE - TILE_BORDER))

def load_piece(location):
  return p.transform.smoothscale(p.image.load(location), (PIECE_SIZE, PIECE_SIZE))