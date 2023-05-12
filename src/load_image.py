import pygame as p

from config import TILE_SIZE

# This function loads an image from a file and scales it to the calculated tile size
def load_image(location):
  return p.transform.scale(p.image.load(location), (TILE_SIZE - 0.5, TILE_SIZE - 0.5))