from game_mechanics import check_draw, check_winner, initialize_board, O_PLAYER, X_PLAYER
from game_ui import display_board, display_help, get_human_player_move


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
                print(f"Badhaai ho, player {current_player}! Aap game jeet gaye.")
                game_is_playing = False
            elif check_draw(board):
                display_board(board)
                print("Game draw ho gaya!")
                game_is_playing = False
            else:
                current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER

        print("Game khatam.")

        again = input("Kya aap dobara khelna chahte hain? (Y/N): ").upper()

        if again == "N":
            break


if __name__ == "__main__":
    play_game()
