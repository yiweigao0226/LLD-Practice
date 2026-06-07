from abc import ABC
class BoardEntity(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end

class Ladder(BoardEntity):
    def __init__(self, start, end):
        super().__init__(start, end)

class Snake(BoardEntity):
    def __init__(self, start, end):
        super().__init__(start, end)