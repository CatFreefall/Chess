import pygame as p

# dimensions of game window
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 680

# general tile colours
BLACK_TILE = p.image.load("assets/Tiles/Tile-Black.png")
WHITE_TILE = p.image.load("assets/Tiles/Tile-White.png")

# tile path images
BLACK_TILE_PATH = p.image.load("assets/Tiles/TilePath-Black.png")
WHITE_TILE_PATH = p.image.load("assets/Tiles/TilePath-White.png")

# piece origin colour
PIECE_ORIGIN = p.image.load("assets/Tiles/Piece-Origin.png")

# piece destination colour
PIECE_DESTINATION = p.image.load("assets/Tiles/Piece-Destination.png")

# white pieces
WHITE_PAWN = p.image.load("assets/WhitePieces/Pawn-White.png")
WHITE_ROOK = p.image.load("assets/WhitePieces/Rook-White.png")
WHITE_KNIGHT = p.image.load("assets/WhitePieces/Knight-White.png")
WHITE_BISHOP = p.image.load("assets/WhitePieces/Bishop-White.png")
WHITE_QUEEN = p.image.load("assets/WhitePieces/Queen-White.png")
WHITE_KING = p.image.load("assets/WhitePieces/King-White.png")

# black pieces
BLACK_PAWN = p.image.load("assets/BlackPieces/Pawn-Black.png")
BLACK_ROOK = p.image.load("assets/BlackPieces/Rook-Black.png")
BLACK_KNIGHT = p.image.load("assets/BlackPieces/Knight-Black.png")
BLACK_BISHOP = p.image.load("assets/BlackPieces/Bishop-Black.png")
BLACK_QUEEN = p.image.load("assets/BlackPieces/Queen-Black.png")
BLACK_KING = p.image.load("assets/BlackPieces/King-Black.png")
