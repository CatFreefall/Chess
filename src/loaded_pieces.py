import pygame as p

from config import PIECE_SIZE
from pieces.Pawn import Pawn
from pieces.Rook import Rook
from pieces.Knight import Knight
from pieces.Bishop import Bishop
from pieces.Queen import Queen
from pieces.King import King

def load_piece(location):
  return p.transform.scale(p.image.load(location), (PIECE_SIZE, PIECE_SIZE))

# white pieces
WHITE_PAWN = Pawn("pawn", "white", load_piece("assets/pieces/white_pieces/Pawn-White.png"))
WHITE_ROOK = Rook("rook", "white", load_piece("assets/pieces/white_pieces/Rook-White.png"))
WHITE_KNIGHT = Knight("knight", "white", load_piece("assets/pieces/white_pieces/Knight-White.png"))
WHITE_BISHOP = Bishop("bishop", "white", load_piece("assets/pieces/white_pieces/Bishop-White.png"))
WHITE_QUEEN = Queen("queen", "white", load_piece("assets/pieces/white_pieces/Queen-White.png"))
WHITE_KING = King("king", "white", load_piece("assets/pieces/white_pieces/King-White.png"))

# black pieces
BLACK_PAWN = Pawn("pawn", "black", load_piece("assets/pieces/black_pieces/Pawn-Black.png"))
BLACK_ROOK = Rook("rook", "black", load_piece("assets/pieces/black_pieces/Rook-Black.png"))
BLACK_KNIGHT = Knight("knight", "black", load_piece("assets/pieces/black_pieces/Knight-Black.png"))
BLACK_BISHOP = Bishop("bishop", "black", load_piece("assets/pieces/black_pieces/Bishop-Black.png"))
BLACK_QUEEN = Queen("queen", "black", load_piece("assets/pieces/black_pieces/Queen-Black.png"))
BLACK_KING = King("king", "black", load_piece("assets/pieces/black_pieces/King-Black.png"))

# creates a new instance of a pawn
def pawn(name):
  if (name == "white"):
    return Pawn("pawn", "white", load_piece("assets/pieces/white_pieces/Pawn-White.png"))
  
  else:
    return Pawn("pawn", "black", load_piece("assets/pieces/black_pieces/Pawn-Black.png"))