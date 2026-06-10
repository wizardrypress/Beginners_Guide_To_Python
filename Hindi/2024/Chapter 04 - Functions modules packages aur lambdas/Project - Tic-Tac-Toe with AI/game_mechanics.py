EMPTY_SPOT = " "
X_PLAYER = "X"
O_PLAYER = "O"


def initialize_board():
    return [EMPTY_SPOT] * 9


def check_draw(board):
    return EMPTY_SPOT not in board


def check_winner(board):
    # Saari possible winning combinations define karo.
    win_conditions = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal
        (2, 4, 6),  # Diagonal
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != EMPTY_SPOT:
            return board[condition[0]]

    return None
