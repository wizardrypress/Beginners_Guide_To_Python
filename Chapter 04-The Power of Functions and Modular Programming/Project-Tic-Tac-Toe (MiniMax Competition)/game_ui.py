import random

from game_ai import random_ai_move


types_of_players = {
    "H": "Human",
    "1": "Random AI",
    "2": "Rule-Based AI",
    "3": "Minimax AI"
}


def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def get_human_player_move(current_player, board):
    # Convert board indexes 0-8 to more user-friendly numbers 1-9
    while True:
        try:
            # Subtracting 1 to account for the shift from 1-9 to 0-8 indexing
            position = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid move. Please choose a number between 1 and 9.")
            elif board[position] != " ":
                print("This space is already taken. Please choose another space.")
            else:
                return position
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_ai_player_move(current_player, ai_level, board):
    if ai_level == 1:
        return random_ai_move(board)
    elif ai_level == 2:
        # Placeholder for Rule-Based AI logic
        pass
    elif ai_level == 3:
        # Placeholder for Minimax AI logic
        pass


def select_player_types():
    print(f"Who are the Players:")

    for key, value in types_of_players.items():
        print(f"{key}: {value}")

    player_types = []
    for i in range(2):
        while True:
            choice = input(f"Player {i+1} (H, 1, 2, 3 or Q): ").upper()
            if choice == "Q":
                return None
            elif choice in ['H', '1', '2', '3']:
                player_types.append(choice)
                break
            else:
                print("Invalid selection. Please choose H, 1, 2, or 3.")

    return player_types


def select_rounds(player_types):
    if "H" in player_types:
        rounds = 1
    else:
        rounds = int(input("How many rounds? "))
    return rounds


def select_first_player(player_types):
    print("First Player:")
    print(f"1. {types_of_players[player_types[0]]}")
    print(f"2. {types_of_players[player_types[1]]}")
    print("R. Random First Player")

    while True:
        choice = input(f"First Player (1, 2, R): ").upper()
        if choice in ['1', '2']:
            return int(choice)-1
        elif choice == "R":
            return random.choice([0, 1])
