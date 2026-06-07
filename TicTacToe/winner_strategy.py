from abc import ABC, abstractmethod
class WinnerStrategy(ABC):
    @abstractmethod
    def check(self, Board, Player):
        pass

class RowWinnerStrategy(WinnerStrategy):
    def check(self, Board, Player):
        for row in range(Board._size):
            win = True
            for col in range(Board._size):
                if Board._board[row][col].get_symbol() != Player.get_symbol():
                    win = False
                    break
            if win:
                return True
        return False

class ColumnWinnerStrategy(WinnerStrategy):
    def check(self, Board, Player):
        for col in range(Board._size):
            win = True
            for row in range(Board._size):
                if Board._board[row][col].get_symbol() != Player.get_symbol():
                    win = False
                    break
            if win:
                return True
        return False

class DiagonalWinnerStrategy(WinnerStrategy):
    def check(self, Board, Player):
        win = True
        for i in range(Board._size):
            if Board._board[i][i].get_symbol() != Player.get_symbol():
                win = False
        if win:
            return True
        for i in range(Board._size):
            if Board._board[i][Board._size - i - 1].get_symbol() != Player.get_symbol():
                win = False
        if win:
            return True
        return False
