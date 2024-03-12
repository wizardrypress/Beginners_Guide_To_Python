import random

from game_ai import get_ai_move
from game_mechanics import check_winner, check_draw
from game_ui import display_board, get_human_player_move, select_player_types, select_rounds


def initialize_board():
    return [" "]*9


def play_game():
    player_types = select_player_types()
    if player_types is None:
        return

    rounds = select_rounds(player_types)
    if rounds is None:
        return

    first_player = 0 #random.choice([0, 1])
    players = {
        "X": player_types[first_player],
        "O": player_types[(first_player + 1) % 2]
    }

    wins = {"X": 0, "O": 0}
    draws = 0
    current_player = "X"

    for i in range(rounds):
        board = initialize_board()
        game_is_playing = True

        print(f"------------------ {i+1} of {rounds} ------------------")

        while game_is_playing:
            display_board(board)
            print(f"Current player: {current_player}")

            if players[current_player] == "H":
                move = get_human_player_move(current_player, board)
            else:
                move = get_ai_move(players[current_player], current_player, board)

            board[move] = current_player

            if check_winner(board):  # Step 4: Check for win
                display_board(board)
                print(f"Congratulations, Player {current_player}! You've won the game.")
                wins[current_player] += 1
                game_is_playing = False
            elif check_draw(board):  # Step 5: Check for draw
                display_board(board)
                print("The game is a draw!")
                draws += 1
                game_is_playing = False
            else:
                current_player = "O" if current_player == "X" else "X"  # Step 6: Switch turns

        print("Game over.")

    print(f"X {players["X"]} = {wins['X']}")
    print(f"O {players["O"]} = {wins['O']}")
    print(f"Draws = {draws}")


if __name__ == "__main__":
    play_game()