from mecanica_juego import check_winner, check_draw, initialize_board, X_PLAYER, O_PLAYER
from game_ui import display_board, get_human_player_move, display_help


def play_game():
    while True:
        board = initialize_board()
        current_player = X_PLAYER
        game_is_playing = True

        display_help(board.copy())

        while game_is_playing:
            display_board(board)

            move = get_human_player_move(current_player, board)

            if move is None:
                break

            board[move] = current_player

            if check_winner(board):
                display_board(board)
                print(f"¡Felicidades, jugador {current_player}! Ganaste el juego.")
                game_is_playing = False
            elif check_draw(board):
                display_board(board)
                print("¡El juego terminó en empate!")
                game_is_playing = False
            else:
                current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER

        print("Juego terminado.")

        again = input("¿Quieres jugar otra vez? (S/N): ").upper()

        if again == "N":
            break


if __name__ == "__main__":
    play_game()
