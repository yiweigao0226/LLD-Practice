from board import Board
from dice import Dice
from player import Player
from game_status import GameStatus
from collections import deque

class Game:
    def __init__(self, players, entities):
        self.board = Board(101, entities)
        self.players = deque()
        for player in players:
            self.players.append(Player(player))
        self.dice = Dice(1, 6)
        self.status = GameStatus.NOT_START
        self.winner = None
    def play(self):
        if len(self.players) < 2:
            print("Cannot start the game, must be at least 2 players.")
            return
        self.status = GameStatus.IN_PROGRESS
        print("Game Start!")
        while self.status == GameStatus.IN_PROGRESS:
            current_player = self.players.popleft()
            self.take_turn(current_player)
            if self.status == GameStatus.IN_PROGRESS:
                self.players.append(current_player)
        print("Game Finished!")
        if self.winner is not None:
            print(f"The winner is {self.winner.get_name()}")
    def take_turn(self, player):
        roll = self.dice.roll()
        print(f"\n{player.get_name()}'s turn. Roll a {roll}")
        current_position = player.get_position()
        next_position = current_position + roll
        if next_position >= self.board.get_size():
            print(f"{player.get_name()} should land exactly on {self.board.get_size() - 1}, turn skipped")
            return
        if next_position == self.board.get_size() - 1:
            player.set_position(next_position)
            self.winner = player
            self.status = GameStatus.FINISH
            print(f"Finally! {player.get_name()} reached the end! The game done!")
            return
        final_position = next_position
        if next_position in self.board.ladder_and_snake:
            final_position = self.board.ladder_and_snake[next_position]
        if final_position > next_position:
            print(f"{player.get_name()} found a ladder at position {next_position} and climb to {final_position}.")
        elif final_position < next_position:
            print(f"{player.get_name()} found a snake at position {next_position} and down to {final_position}.")
        else:
            print(f"{player.get_name()} moved from {current_position} to {final_position}.")
        player.set_position(final_position)
        