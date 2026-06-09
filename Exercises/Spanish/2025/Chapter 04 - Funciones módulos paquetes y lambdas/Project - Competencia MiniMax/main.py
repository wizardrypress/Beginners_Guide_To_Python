from game_ai import get_ai_move
from game_mechanics import check_winner, check_draw, initialize_board, X_PLAYER, O_PLAYER
from game_ui import (
    display_board,
    get_human_player_move,
    select_player_types,
    select_rounds,
    select_first_player,
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

        print(f"------------------ {round_number + 1} de {rounds} ------------------")

        while game_is_playing:
            display_board(board)
            print(f"Jugador actual: {current_player}")

            if players[current_player] == "H":
                move = get_human_player_move(current_player, board)
            else:
                move = get_ai_move(players[current_player], current_player, board)
                print(f"{types_of_players[players[current_player]]} eligió la posición {move + 1}.")

            board[move] = current_player

            if check_winner(board):
                display_board(board)
                print(f"¡Felicidades, jugador {current_player}! Ganaste el juego.")
                wins[current_player] += 1
                game_is_playing = False
            elif check_draw(board):
                display_board(board)
                print("¡El juego terminó en empate!")
                draws += 1
                game_is_playing = False
            else:
                current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER

        print("Juego terminado.")

    print(f"Victorias de {X_PLAYER} ({types_of_players[players[X_PLAYER]]}): {wins[X_PLAYER]}")
    print(f"Victorias de {O_PLAYER} ({types_of_players[players[O_PLAYER]]}): {wins[O_PLAYER]}")
    print(f"Número de empates: {draws}")


if __name__ == "__main__":
    play_game()
