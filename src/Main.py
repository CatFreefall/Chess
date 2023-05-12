import pygame as p
from Config import *

p.init()

gameWindow = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
  for event in p.event.get():
    if event.type == p.QUIT:
      p.quit()
      quit()