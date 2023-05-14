from loaded_assets.loaded_tiles import *
from loaded_assets.loaded_pieces import *
from Tile import Tile

game_board = [
    [Tile(WHITE_TILE_8), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE)],
    [Tile(BLACK_TILE_7), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE)],
    [Tile(WHITE_TILE_6), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE)],
    [Tile(BLACK_TILE_5), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE)],
    [Tile(WHITE_TILE_4), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE)],
    [Tile(BLACK_TILE_3), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE)],
    [Tile(WHITE_TILE_2), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE), Tile(WHITE_TILE), Tile(BLACK_TILE)],
    [Tile(BLACK_TILE_1A), Tile(WHITE_TILE_B), Tile(BLACK_TILE_C), Tile(WHITE_TILE_D), Tile(BLACK_TILE_E), Tile(WHITE_TILE_F), Tile(BLACK_TILE_G), Tile(WHITE_TILE_H)]
]

game_pieces = [
  [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_KING, BLACK_QUEEN, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK],
  [BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN],
  ["________", "________", "________", "________", "________", "________", "________", "________"],
  ["________", "________", "________", "________", "________", "________", "________", "________"],
  ["________", "________", "________", "________", "________", "________", "________", "________"],
  ["________", "________", "________", "________", "________", "________", "________", "________"],
  [WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN],
  [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_KING, WHITE_QUEEN, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK]
]