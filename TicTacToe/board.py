from symbol import Symbol
from cell import Cell
class Board:
    def __init__(self, size):
        self._size = size
        self._board = []
        self.move_count = 0
        self.initialize_board()
    def initialize_board(self):
        self._board = [[Cell() for _ in range(self._size)] for _ in range(self._size)]
    def place_symbol(self, row, col, symbol):
        if 0 <= row < self._size and 0 <= col < self._size and self._board[row][col].get_symbol() == Symbol.EMPTY:
            self._board[row][col].set_symbol(symbol)
            self.move_count += 1
    def is_full(self):
        if self.move_count == self._size * self._size:
            return True
        return False