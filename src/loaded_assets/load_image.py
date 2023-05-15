import pygame as p

from config import TILE_SIZE, PIECE_SIZE, TILE_BORDER

# Theis function loads the piece from a file, increases its quality, and scales them to PIECE_SIZE
# def load_tile(location):
  # return p.transform.smoothscale(p.image.load(location), (TILE_SIZE - TILE_BORDER, TILE_SIZE - TILE_BORDER))

def load_piece(location):
  return p.transform.scale(p.image.load(location), (PIECE_SIZE, PIECE_SIZE))