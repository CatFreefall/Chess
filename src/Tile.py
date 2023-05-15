import pygame as p

class Tile(p.Rect):
  def __init__(self, dimensions, colour):
    p.Rect.__init__(self, dimensions)
    self.colour = colour
    self.is_clicked = False
    self.piece = None