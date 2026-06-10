from game_ai import get_ai_move
from game_mechanics import check_draw, check_winner, initialize_board, O_PLAYER, X_PLAYER
from game_ui import (
    display_board,
    get_human_player_move,
    select_first_player,
    select_player_types,
    select_rounds,
    types_of_players,
)


def play_game():
    player_types = select_player_types()

    if player_types is None:
        return

    rounds = select_rounds(player_types)

    if rounds is None:
        return

    first_player = select_first_player(player_types)

    players = {
        X_PLAYER: player_types[first_player],
        O_PLAYER: player_types[(first_player + 1) % 2],
    }

    wins = {X_PLAYER: 0, O_PLAYER: 0}
    draws = 0

    for round_number in range(rounds):
        board = initialize_board()
        current_player = X_PLAYER
        game_is_playing = True

        print(f"------------------ {round_number + 1} of {rounds} ------------------")

        while game_is_playing:
            display_board(board)
            print(f"Current player: {current_player}")

            if players[current_player] == "H":
                move = get_human_player_move(current_player, board)
            else:
                move = get_ai_move(players[current_player], current_player, board)
                print(f"{types_of_players[players[current_player]]} ne position {move + 1} choose ki.")

            board[move] = current_player

            if check_winner(board):
                display_board(board)
                print(f"Badhaai ho, player {current_player}! Aap game jeet gaye.")
                wins[current_player] += 1
                game_is_playing = False
            elif check_draw(board):
                display_board(board)
                print("Game draw ho gaya!")
                draws += 1
                game_is_playing = False
            else:
                current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER

        print("Game khatam.")

    print(f"{X_PLAYER} ki wins ({types_of_players[players[X_PLAYER]]}): {wins[X_PLAYER]}")
    print(f"{O_PLAYER} ki wins ({types_of_players[players[O_PLAYER]]}): {wins[O_PLAYER]}")
    print(f"Draws ki sankhya: {draws}")


if __name__ == "__main__":
    play_game()
