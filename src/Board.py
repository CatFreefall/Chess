import pygame as p

from config import TILE_SIZE
from tiles import BLACK_TILE, WHITE_TILE

def initializeBoard (gameWindow):

  gameBoard = [
    ["8", "-", "+", "-", "+", "-", "+", "-"],
    ["7", "+", "-", "+", "-", "+", "-", "+"],
    ["6", "-", "+", "-", "+", "-", "+", "-"],
    ["5", "+", "-", "+", "-", "+", "-", "+"],
    ["4", "-", "+", "-", "+", "-", "+", "-"],
    ["3", "+", "-", "+", "-", "+", "-", "+"],
    ["2", "-", "+", "-", "+", "-", "+", "-"],
    ["1", "b", "c", "d", "e", "f", "g", "h"],
  ]

  gameWindow.fill(p.Color("white"))

  for i in range(0, 8):
    for j in range(0, 8):
      if (i + j) % 2 == 0:
        gameWindow.blit(WHITE_TILE, (i * TILE_SIZE, j * TILE_SIZE))
      else:
        gameWindow.blit(BLACK_TILE, (i * TILE_SIZE, j * TILE_SIZE))