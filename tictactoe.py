from board import Board
from player import Player
from cell import Cell
from symbol import Symbol
from game_status import GameStatus
from winner_strategy import ( RowWinnerStrategy, ColumnWinnerStrategy, DiagonalWinnerStrategy )

class TicTacToe:
    def __init__(self):
        self.board = Board(3)
        self.player = [Player("Player_1", Symbol.X), Player("Player_2", Symbol.O)]
        self.current_player = 0
        self.current_status = GameStatus.IN_PROGRESS
        self.winner = None
        self.win_check = [RowWinnerStrategy(), ColumnWinnerStrategy(), DiagonalWinnerStrategy()]
    def play_move(self, row, col):
        current_player = self.player[self.current_player]
        self.board.place_symbol(row, col, current_player.get_symbol())
        for strategy in self.win_check:
            if strategy.check(self.board, current_player):
                self.winner = current_player
                if self.current_player == 0:
                    self.current_status = GameStatus.PLAYER_1_WIN
                else:
                    self.current_status = GameStatus.PLAYER_2_WIN
                return
        if self.board.is_full():
            self.current_status = GameStatus.DRAW
        self.current_player = 1 - self.current_player