import random

from game_mechanics import check_winner, EMPTY_SPOT, O_PLAYER, X_PLAYER


def test_move(board, player, position):
    temp_board = board.copy()
    temp_board[position] = player

    return check_winner(temp_board) == player


def get_rules_based_ai_move(computer_player, board):
    # Pehle jeetne ki koshish karo.
    for index in range(9):
        if board[index] == EMPTY_SPOT and test_move(board, computer_player, index):
            return index

    # Agar opponent jeetne wala hai, use block karo.
    human_player = X_PLAYER if computer_player == O_PLAYER else O_PLAYER

    for index in range(9):
        if board[index] == EMPTY_SPOT and test_move(board, human_player, index):
            return index

    # Center ya corner lene ki koshish karo.
    preferred_positions = [4, 0, 2, 6, 8]
    random.shuffle(preferred_positions)

    for index in preferred_positions:
        if board[index] == EMPTY_SPOT:
            return index

    # Agar clear strategy nahi hai, random move choose karo.
    available_spots = [
        index for index in range(9)
        if board[index] == EMPTY_SPOT
    ]

    return random.choice(available_spots)
