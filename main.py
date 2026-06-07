from tictactoe import TicTacToe
from game_status import GameStatus

def print_board(board):
    for row in board._board:
        print(" | ".join(cell.get_symbol().value for cell in row))
    print()

game = TicTacToe()

while game.current_status == GameStatus.IN_PROGRESS:
    print_board(game.board)

    current_player = game.player[game.current_player]
    print(f"{current_player.get_name()}'s turn")

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))

    game.play_move(row, col)

print_board(game.board)

if game.current_status == GameStatus.DRAW:
    print("Game Draw")
else:
    print(f"{game.winner.get_name()} Wins!")