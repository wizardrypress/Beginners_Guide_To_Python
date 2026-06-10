import random

from game_ai import random_ai_move


types_of_players = {
    "H": "Human",
    "1": "Random AI",
    "2": "Rules-based AI",
    "3": "MiniMax AI",
}


def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def get_human_player_move(current_player, board):
    # Board indexes 0-8 hote hain; player ke liye unhe 1-9 bana rahe hain.
    while True:
        try:
            position = int(input(f"Player {current_player}, apna move enter karo (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Invalid move. 1 se 9 ke beech number choose karo.")
            elif board[position] != " ":
                print("Ye space already occupied hai. Koi aur space choose karo.")
            else:
                return position
        except ValueError:
            print("Invalid input. Ek number enter karo.")


def get_ai_player_move(current_player, ai_level, board):
    if ai_level == 1:
        return random_ai_move(board)

    # Ye function extension example ke roop me rakha gaya hai.
    # Actual AI selection get_ai_move() me hoti hai.
    return random_ai_move(board)


def select_player_types():
    print("Players kaun honge?")

    for key, value in types_of_players.items():
        print(f"{key}: {value}")

    player_types = []

    for player_number in range(2):
        while True:
            choice = input(f"Player {player_number + 1} (H, 1, 2, 3 ya Q): ").upper()

            if choice == "Q":
                return None
            elif choice in ["H", "1", "2", "3"]:
                player_types.append(choice)
                break
            else:
                print("Invalid selection. H, 1, 2, ya 3 choose karo.")

    return player_types


def select_rounds(player_types):
    if "H" in player_types:
        return 1

    while True:
        try:
            rounds = int(input("Kitne rounds? "))

            if rounds <= 0:
                print("Zero se bada number enter karo.")
            else:
                return rounds
        except ValueError:
            print("Invalid input. Ek number enter karo.")


def select_first_player(player_types):
    print("First player:")
    print(f"1. {types_of_players[player_types[0]]}")
    print(f"2. {types_of_players[player_types[1]]}")
    print("R. Random first player")

    while True:
        choice = input("First player (1, 2, R): ").upper()

        if choice in ["1", "2"]:
            return int(choice) - 1
        elif choice == "R":
            return random.choice([0, 1])
        else:
            print("Invalid selection. 1, 2, ya R choose karo.")
