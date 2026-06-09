EMPTY_SPOT = " "
X_PLAYER = "X"
O_PLAYER = "O"


def initialize_board():
    return [EMPTY_SPOT] * 9


def check_draw(board):
    return EMPTY_SPOT not in board


def check_winner(board):
    # Define todas las combinaciones ganadoras posibles.
    win_conditions = [
        (0, 1, 2),  # Fila superior
        (3, 4, 5),  # Fila central
        (6, 7, 8),  # Fila inferior
        (0, 3, 6),  # Columna izquierda
        (1, 4, 7),  # Columna central
        (2, 5, 8),  # Columna derecha
        (0, 4, 8),  # Diagonal
        (2, 4, 6),  # Diagonal
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != EMPTY_SPOT:
            return board[condition[0]]

    return None
