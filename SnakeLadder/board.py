from board_entity import BoardEntity
class Board:
    def __init__(self, size, entities):
        self.size = size
        self.ladder_and_snake = {}
        self.entities = entities
        self.initialize_board()
    def initialize_board(self):
        for entity in self.entities:
            self.ladder_and_snake[entity.get_start()] = entity.get_end()
    def get_size(self):
        return self.size