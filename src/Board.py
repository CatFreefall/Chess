import pygame as p

from config import TILE_SIZE
from tiles import *

def initializeBoard (gameWindow):

  gameBoard = [
    [WHITE_TILE_8, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE],
    [BLACK_TILE_7, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE],
    [WHITE_TILE_6, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE],
    [BLACK_TILE_5, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE],
    [WHITE_TILE_4, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE],
    [BLACK_TILE_3, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE],
    [WHITE_TILE_2, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE, WHITE_TILE, BLACK_TILE],
    [BLACK_TILE_1A, WHITE_TILE_B, BLACK_TILE_C, WHITE_TILE_D, BLACK_TILE_E, WHITE_TILE_F, BLACK_TILE_G, WHITE_TILE_H]
  ]

  gameWindow.fill(p.Color("white"))

  for i in range(0, len(gameBoard)):
    for j in range(0, len(gameBoard[i])):
      gameWindow.blit(gameBoard[j][i], (i * TILE_SIZE, j * TILE_SIZE))
      
#  for i in range(0, 8):
#    for j in range(0, 8):
#      if (i + j) % 2 == 0:
#        gameWindow.blit(WHITE_TILE, (i * TILE_SIZE, j * TILE_SIZE))
#      else:
#        gameWindow.blit(BLACK_TILE, (i * TILE_SIZE, j * TILE_SIZE))
