import random

from game_mechanics import check_winner, check_draw, initialize_board, X_PLAYER, O_PLAYER
from game_ui import display_board, get_human_player_move, display_help
from game_ai import get_rules_based_ai_move


def play_game():
    while True:
        board = initialize_board()
        current_player = X_PLAYER
        computer_player = random.choice([X_PLAYER, O_PLAYER])
        game_is_playing = True

        display_help(board.copy())
        print(f"La computadora jugará como {computer_player}.")

        while game_is_playing:
            if current_player == computer_player:
                move = get_rules_based_ai_move(computer_player, board)
                print(f"La computadora eligió la posición {move + 1}.")
            else:
                display_board(board)

                move = get_human_player_move(current_player, board)

                if move is None:
                    break

            board[move] = current_player

            if check_winner(board):
                display_board(board)

                if current_player == computer_player:
                    print("La computadora ganó esta partida.")
                else:
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
