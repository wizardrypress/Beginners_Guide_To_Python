def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def display_help(board):
    print("""
Tic-Tac-Toe is a simple yet fun game where two players take turns marking 
spaces in a 3x3 grid with their chosen symbol, either an "X" or an "O". 
The goal is to be the first to get three of your symbols aligned either 
horizontally, vertically, or diagonally.

To play, just select an empty spot on the grid by entering its corresponding 
number when it's your turn. Remember, strategy is key—block your opponent's 
moves while aiming to complete your line of three. Good luck, and may the best 
strategist win!

Available positions are:
""")
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = str(i+1)

    display_board(board)


def get_human_player_move(current_player, board):
    # Convert board indexes 0-8 to more user-friendly numbers 1-9
    while True:
        print(f"Player {current_player}")
        move = input("What is your move (1-9, or H-help , Q-quit): ")
        if move.isnumeric():
            position = int(move) - 1
            if position < 0 or position > 8:
                print("Invalid move. Please choose a number between 1 and 9.")
            elif board[position] != " ":
                print("This space is already taken. Please choose another space.")
            else:
                return position
        else:
            match move.upper():
                case "H": display_help(board.copy())
                case "Q": return None
                case _: print("Invalid input. Please enter a number between 1 and 9.")


def select_ai_level():
    print("Who is your opponent:")
    print("1: Random AI")
    print("2: Rule-Based AI")
    print("Q: Quit")

    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice.upper() == "Q":
            return None
        if choice in ['1', '2']:
            return int(choice)
        else:
            print("Invalid selection. Please choose 1, 2 or Q")
