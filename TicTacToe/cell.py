from symbol import Symbol
class Cell:
    def __init__(self):
        self._symbol = Symbol.EMPTY
    def set_symbol(self, symbol):
        self._symbol = symbol
    def get_symbol(self):
        return self._symbol