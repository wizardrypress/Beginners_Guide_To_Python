import random

from game_mechanics import get_available_spots, check_winner, EMPTY_SPOT, X_PLAYER, O_PLAYER


def get_ai_move(ai_type, current_player, board):
    if ai_type == "1":
        return random_ai_move(board)
    elif ai_type == "2":
        return rules_based_ai_move(current_player, board)
    elif ai_type == "3":
        return minimax_ai_move_V2(current_player, board)


def random_ai_move(board):
    available_spots = get_available_spots(board)
    return random.choice(available_spots) if available_spots else None


def test_move(board, player, position):
    """
    Simulates a move on the board for a given player at a given position.
    Returns True if this move results in a win for the player.
    """
    temp_board = board.copy()
    temp_board[position] = player
    return check_winner(temp_board) == player


def rules_based_ai_move(current_player, board):
    """
    Determines the AI's move based on predefined rules.
    """
    opponent = O_PLAYER if current_player == X_PLAYER else X_PLAYER

    # Try for a Win
    for i in range(9):
        if board[i] == EMPTY_SPOT and test_move(board, current_player, i):
            return i

    # Block Opponent
    for i in range(9):
        if board[i] == EMPTY_SPOT and test_move(board, opponent, i):
            return i

    # Try Center or Corners
    corners = [0, 2, 6, 8, 4]
    random.shuffle(corners)
    for i in corners:
        if board[i] == EMPTY_SPOT:
            return i

    # Pick Randomly
    return random.choice(get_available_spots(board))


def minimax_V1(board, is_maximizing, current_player, depth=0):
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
            score, _ = minimax_V1(board, False, current_player, depth + 1)
            board[spot] = EMPTY_SPOT
            if score > best_score:
                best_score = score
                best_move = spot
        return best_score, best_move
    else:
        best_score = float("inf")
        best_move = None
        for spot in get_available_spots(board):
            board[spot] = opponent
            score, _ = minimax_V1(board, True, current_player, depth + 1)
            board[spot] = EMPTY_SPOT
            if score < best_score:
                best_score = score
                best_move = spot
        return best_score, best_move

def minimax_ai_move_V1(current_player, board):
    _, best_move = minimax_V1(board, True, current_player)
    return best_move


def minimax_V2(player, board, depth, is_maximizing):
    opponent = O_PLAYER if player == X_PLAYER else X_PLAYER
    if check_winner(board) == player:
        return 10 - depth, None  # Prioritize quicker wins
    elif check_winner(board) == opponent:
        return depth - 10, None  # Less penalty for slower losses
    elif len(get_available_spots(board)) == 0:
        return 0, None

    best_score = float('-inf') if is_maximizing else float('inf')
    best_move = None
    for move in get_available_spots(board):
        board[move] = player if is_maximizing else opponent
        score, _ = minimax_V2(player, board, depth + 1, not is_maximizing)
        board[move] = EMPTY_SPOT

        if is_maximizing and score > best_score or not is_maximizing and score < best_score:
            best_score = score
            best_move = move

    return best_score, best_move


def minimax_ai_move_V2(player, board):
    # If it's the first move of the game, choose an optimal position randomly
    # to introduce variability and avoid predictability
    if len(get_available_spots(board)) == 9:
        return random.choice([0, 2, 6, 8])  # Corner positions are generally considered optimal first moves

    _, move = minimax_V2(player, board, 0, True)
    return move
