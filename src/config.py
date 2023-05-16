#TODO: Change config.py to a config.cfg file

# note that GAME_WIDTH, GAME_HEIGHT_ TILE_BORDER, PIECE_SIZE, and WINDOW_BORDER can be manipulated

# dimensions of the game (excluding window borders)
GAME_SIZE = 640

# dimensions of each tile
TILE_SIZE = GAME_SIZE // 8

# size of border between each tile
TILE_BORDER = 0.5

# dimensions of each piece
PIECE_SIZE = TILE_SIZE * 0.7

# borders of each piece relative to a tile
PIECE_BORDER = (TILE_SIZE - PIECE_SIZE - TILE_BORDER) // 2

# window border
WINDOW_BORDER = GAME_SIZE // 100

# dimensions of the game window (includes borders)
WINDOW_SIZE = GAME_SIZE + (WINDOW_BORDER * 2) - TILE_BORDER

# tile colours
TILE_BLACK = (183, 192, 216)
TILE_WHITE = (232, 237, 249)

TILE_ORIGIN = (177, 167, 252)
TILE_DESTINATION = (153, 144, 236)

TILE_CAPTURE = (230, 97, 97)