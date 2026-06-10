from game_mechanics import EMPTY_SPOT


def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def display_help(board):
    print("""
Tic-Tac-Toe ek simple aur fun game hai. Is version me aap computer ke
against khelenge.

Computer basic rules use karega: jeetne ki koshish, aapko block karna,
aur achhi positions choose karna.

Khelne ke liye apni turn par khali position ka number enter karo.

Available positions:
""")

    for index in range(len(board)):
        if board[index] == EMPTY_SPOT:
            board[index] = str(index + 1)

    display_board(board)


def get_human_player_move(current_player, board):
    # Board indexes 0-8 hote hain; player ke liye unhe 1-9 bana rahe hain.
    while True:
        move = input(
            f"Player {current_player} - apna move enter karo "
            "(1-9, H-help, Q-quit): "
        )

        if move.isnumeric():
            position = int(move) - 1

            if position < 0 or position > 8:
                print("Invalid move. 1 se 9 ke beech number choose karo.")
            elif board[position] != EMPTY_SPOT:
                print("Ye space already occupied hai. Koi aur space choose karo.")
            else:
                return position
        else:
            match move.upper():
                case "H":
                    display_help(board.copy())
                case "Q":
                    return None
                case _:
                    print("Invalid input. 1 se 9 ke beech number enter karo.")
