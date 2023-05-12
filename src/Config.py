import pygame as p

# dimensions of game window
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 680

# general tile colours
BLACK_TILE = p.image.load("assets/Tiles/Tile_Black.png")
WHITE_TILE = p.image.load("assets/Tiles/Tile_White.png")

# tile path images
BLACK_TILE_PATH = p.image.load("assets/Tiles/TilePath_Black.png")
WHITE_TILE_PATH = p.image.load("assets/Tiles/TilePath_White.png")

# piece origin colour
PIECE_ORIGIN = p.image.load("assets/Tiles/Piece_Origin.png")

# piece destination colour
PIECE_DESTINATION = p.image.load("assets/Tiles/Piece_Destination.png")

# white pieces
WHITE_PAWN = p.image.load("assets/WhitePieces/Pawn_White.png")
WHITE_ROOK = p.image.load("assets/WhitePieces/Rook_White.png")
WHITE_KNIGHT = p.image.load("assets/WhitePieces/Knight_White.png")
WHITE_BISHOP = p.image.load("assets/WhitePieces/Bishop_White.png")
WHITE_QUEEN = p.image.load("assets/WhitePieces/Queen_White.png")
WHITE_KING = p.image.load("assets/WhitePieces/King_White.png")

# black pieces
BLACK_PAWN = p.image.load("assets/BlackPieces/Pawn_Black.png")
BLACK_ROOK = p.image.load("assets/BlackPieces/Rook_Black.png")
BLACK_KNIGHT = p.image.load("assets/BlackPieces/Knight_Black.png")
BLACK_BISHOP = p.image.load("assets/BlackPieces/Bishop_Black.png")
BLACK_QUEEN = p.image.load("assets/BlackPieces/Queen_Black.png")
BLACK_KING = p.image.load("assets/BlackPieces/King_Black.png")