import pygame as p

from config import WINDOW_WIDTH, WINDOW_HEIGHT
from board import initializeBoard

p.init()

gameWindow = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
  for event in p.event.get():
    if event.type == p.QUIT:
      p.quit()
      quit()
    else:
      initializeBoard(gameWindow)
      p.display.update()