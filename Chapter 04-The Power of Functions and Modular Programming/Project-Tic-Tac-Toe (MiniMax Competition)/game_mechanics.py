EMPTY_SPOT = " "
X_PLAYER = "X"
O_PLAYER = "O"


def initialize_board():
    return [EMPTY_SPOT] * 9


def check_draw(board):
    return EMPTY_SPOT not in board


def check_winner(board):
    # Define all possible winning combinations
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != EMPTY_SPOT:
            return board[condition[0]]

    return None


def get_available_spots(board):
    return [index for index, spot in enumerate(board) if spot == EMPTY_SPOT]
