from game import Game
from board_entity import ( Ladder, Snake )

class main:
    def main():
        board_entities = [
            Snake(17, 7), Snake(54, 34),
            Snake(62, 19), Snake(98, 79),
            Ladder(3, 38), Ladder(24, 33),
            Ladder(42, 93), Ladder(72, 84)
        ]
        players = ["Lily", "Bob"]
        game = Game(players, board_entities)
        game.play()

    if __name__ == "__main__":
        main()