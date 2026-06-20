import random

from game_ai import random_ai_move


types_of_players = {
    "H": "Humano",
    "1": "IA aleatoria",
    "2": "IA basada en reglas",
    "3": "IA MiniMax",
}


def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def get_human_player_move(current_player, board):
    # Convierte los índices 0-8 del tablero en números 1-9 más fáciles de usar.
    while True:
        try:
            position = int(input(f"Jugador {current_player}, ingresa tu movimiento (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Movimiento inválido. Elige un número entre 1 y 9.")
            elif board[position] != " ":
                print("Ese espacio ya está ocupado. Elige otro espacio.")
            else:
                return position
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


def get_ai_player_move(current_player, ai_level, board):
    if ai_level == 1:
        return random_ai_move(board)

    # Esta función se conserva como ejemplo de extensión.
    # La selección real de IA se hace en get_ai_move().
    return random_ai_move(board)


def select_player_types():
    print("¿Quiénes son los jugadores?")

    for key, value in types_of_players.items():
        print(f"{key}: {value}")

    player_types = []

    for player_number in range(2):
        while True:
            choice = input(f"Jugador {player_number + 1} (H, 1, 2, 3 o Q): ").upper()

            if choice == "Q":
                return None
            elif choice in ["H", "1", "2", "3"]:
                player_types.append(choice)
                break
            else:
                print("Selección inválida. Elige H, 1, 2 o 3.")

    return player_types


def select_rounds(player_types):
    if "H" in player_types:
        return 1

    while True:
        try:
            rounds = int(input("¿Cuántas rondas? "))

            if rounds <= 0:
                print("Ingresa un número mayor que cero.")
            else:
                return rounds
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


def select_first_player(player_types):
    print("Primer jugador:")
    print(f"1. {types_of_players[player_types[0]]}")
    print(f"2. {types_of_players[player_types[1]]}")
    print("R. Primer jugador aleatorio")

    while True:
        choice = input("Primer jugador (1, 2, R): ").upper()

        if choice in ["1", "2"]:
            return int(choice) - 1
        elif choice == "R":
            return random.choice([0, 1])
        else:
            print("Selección inválida. Elige 1, 2 o R.")
