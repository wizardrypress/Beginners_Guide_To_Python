import random

from game_mechanics import get_available_spots, check_winner, EMPTY_SPOT, O_PLAYER, X_PLAYER


def get_ai_move(ai_type, current_player, board):
    if ai_type == "1":
        return random_ai_move(board)
    elif ai_type == "2":
        return rules_based_ai_move(current_player, board)
    elif ai_type == "3":
        return minimax_ai_move_v2(current_player, board)

    return random_ai_move(board)


def random_ai_move(board):
    available_spots = get_available_spots(board)
    return random.choice(available_spots) if available_spots else None


def test_move(board, player, position):
    """
    Board par ek move simulate karta hai.
    Agar is move se player jeetta hai to True return hota hai.
    """
    temp_board = board.copy()
    temp_board[position] = player

    return check_winner(temp_board) == player


def rules_based_ai_move(current_player, board):
    """
    Simple rules use karke AI ka move choose karta hai.
    """
    opponent = O_PLAYER if current_player == X_PLAYER else X_PLAYER

    # Pehle jeetne ki koshish karo.
    for index in range(9):
        if board[index] == EMPTY_SPOT and test_move(board, current_player, index):
            return index

    # Agar opponent jeetne wala hai, use block karo.
    for index in range(9):
        if board[index] == EMPTY_SPOT and test_move(board, opponent, index):
            return index

    # Center ya corner lene ki koshish karo.
    preferred_positions = [4, 0, 2, 6, 8]
    random.shuffle(preferred_positions)

    for index in preferred_positions:
        if board[index] == EMPTY_SPOT:
            return index

    # Agar clear move nahi hai, random move choose karo.
    return random.choice(get_available_spots(board))


def minimax_v1(board, is_maximizing, current_player, depth=0):
    opponent = O_PLAYER if current_player == X_PLAYER else X_PLAYER

    if check_winner(board) == current_player:
        return 10 - depth, None
    elif check_winner(board) == opponent:
        return -10 + depth, None
    elif len(get_available_spots(board)) == 0:
        return 0, None

    if is_maximizing:
        best_score = float("-inf")
        best_move = None

        for spot in get_available_spots(board):
            board[spot] = current_player
            score, _ = minimax_v1(board, False, current_player, depth + 1)
            board[spot] = EMPTY_SPOT

            if score > best_score:
                best_score = score
                best_move = spot

        return best_score, best_move

    best_score = float("inf")
    best_move = None

    for spot in get_available_spots(board):
        board[spot] = opponent
        score, _ = minimax_v1(board, True, current_player, depth + 1)
        board[spot] = EMPTY_SPOT

        if score < best_score:
            best_score = score
            best_move = spot

    return best_score, best_move


def minimax_ai_move_v1(current_player, board):
    _, best_move = minimax_v1(board, True, current_player)
    return best_move


def minimax_v2(player, board, depth, is_maximizing):
    opponent = O_PLAYER if player == X_PLAYER else X_PLAYER

    if check_winner(board) == player:
        return 10 - depth, None
    elif check_winner(board) == opponent:
        return depth - 10, None
    elif len(get_available_spots(board)) == 0:
        return 0, None

    best_score = float("-inf") if is_maximizing else float("inf")
    best_move = None

    for move in get_available_spots(board):
        board[move] = player if is_maximizing else opponent
        score, _ = minimax_v2(player, board, depth + 1, not is_maximizing)
        board[move] = EMPTY_SPOT

        if is_maximizing and score > best_score:
            best_score = score
            best_move = move
        elif not is_maximizing and score < best_score:
            best_score = score
            best_move = move

    return best_score, best_move


def minimax_ai_move_v2(player, board):
    # Pehli move par random corner choose karo.
    # Corners aksar strong starting positions hoti hain.
    if len(get_available_spots(board)) == 9:
        return random.choice([0, 2, 6, 8])

    _, move = minimax_v2(player, board, 0, True)

    return move
