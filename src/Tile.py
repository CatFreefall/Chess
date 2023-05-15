import pygame as p

class Tile(p.Rect):
  def __init__(self, dimensions, colour):
    p.Rect.__init__(self, dimensions)
    self.is_occupied = False
    self.colour = colour
    self.is_clicked = False