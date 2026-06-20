from mecanica_juego import EMPTY_SPOT


def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def display_help(board):
    print("""
El juego del gato es un juego sencillo y divertido en el que dos jugadores
se turnan para marcar espacios en una cuadrícula de 3 x 3 usando "X" u "O".

El objetivo es ser el primero en colocar tres símbolos en línea, ya sea
horizontal, vertical o diagonalmente.

Para jugar, elige una posición vacía escribiendo el número correspondiente
cuando sea tu turno. Recuerda: la estrategia importa. Bloquea los movimientos
de tu oponente mientras intentas completar tu propia línea de tres.

Posiciones disponibles:
""")

    for index in range(len(board)):
        if board[index] == EMPTY_SPOT:
            board[index] = str(index + 1)

    display_board(board)


def get_human_player_move(current_player, board):
    # Convierte los índices 0-8 del tablero en números 1-9 más fáciles de usar.
    while True:
        move = input(
            f"Jugador {current_player} - Ingresa tu movimiento "
            "(1-9, H-ayuda, Q-salir): "
        )

        if move.isnumeric():
            position = int(move) - 1

            if position < 0 or position > 8:
                print("Movimiento inválido. Elige un número entre 1 y 9.")
            elif board[position] != EMPTY_SPOT:
                print("Ese espacio ya está ocupado. Elige otro espacio.")
            else:
                return position
        else:
            match move.upper():
                case "H":
                    display_help(board.copy())
                case "Q":
                    return None
                case _:
                    print("Entrada inválida. Ingresa un número entre 1 y 9.")
