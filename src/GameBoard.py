
# singleton class. this class holds the game state of the board
class GameBoard:
  instance = None

  def __new__(cls):
      if not cls.instance:
          cls.instance = super().__new__(cls)
      return cls.instance

  def __init__(self):
    self.game_board = [
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None],
      [None, None, None, None, None, None, None, None]
    ]