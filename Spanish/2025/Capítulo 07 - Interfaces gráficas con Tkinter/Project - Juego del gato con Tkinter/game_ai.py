import random

from game_mechanics import check_winner, EMPTY_SPOT, X_PLAYER, O_PLAYER


def test_move(board, player, position):
    temp_board = board.copy()
    temp_board[position] = player

    return check_winner(temp_board) == player


def get_rules_based_ai_move(computer_player, board):
    # Intenta ganar.
    for index in range(9):
        if board[index] == EMPTY_SPOT and test_move(board, computer_player, index):
            return index

    # Bloquea al oponente si está a punto de ganar.
    human_player = X_PLAYER if computer_player == O_PLAYER else O_PLAYER

    for index in range(9):
        if board[index] == EMPTY_SPOT and test_move(board, human_player, index):
            return index

    # Intenta tomar el centro o una esquina.
    preferred_positions = [4, 0, 2, 6, 8]
    random.shuffle(preferred_positions)

    for index in preferred_positions:
        if board[index] == EMPTY_SPOT:
            return index

    # Si no hay una jugada estratégica clara, elige al azar.
    available_spots = [
        index for index in range(9)
        if board[index] == EMPTY_SPOT
    ]

    return random.choice(available_spots)
