import pygame as p

from config import TILE_SIZE, WINDOW_BORDER, PIECE_BORDER
from image_arrays import *

def initializeBoard (gameWindow):
  gameWindow.fill(p.Color("white"))

  for i in range(0, len(gameBoard)):
    for j in range(0, len(gameBoard[i])):

      # generating tiles including the ones with coordinates
      tileCoordX = i * TILE_SIZE + WINDOW_BORDER
      tileCoordY = j * TILE_SIZE + WINDOW_BORDER
      gameWindow.blit(gameBoard[j][i].convert(), (tileCoordX, tileCoordY))

      # generating pieces
      if (gamePieces[j][i] != "________"):
        pieceCoordX = tileCoordX + PIECE_BORDER
        pieceCoordY = tileCoordY + PIECE_BORDER
        gameWindow.blit(gamePieces[j][i].convert_alpha(), (pieceCoordX, pieceCoordY))