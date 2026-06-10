import random
import tkinter as tk
from tkinter import messagebox

from game_ai import get_rules_based_ai_move
from game_mechanics import (
    check_draw,
    check_winner,
    initialize_board,
    EMPTY_SPOT,
    X_PLAYER,
    O_PLAYER,
)


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe with Tkinter")
        self.root.resizable(False, False)

        self.board = initialize_board()
        self.current_player = X_PLAYER
        self.human_player = X_PLAYER
        self.computer_player = O_PLAYER
        self.game_over = False

        self.status_label = tk.Label(
            root,
            text="Aapki turn.",
            font=("Arial", 14),
            pady=10,
        )
        self.status_label.grid(row=0, column=0, columnspan=3)

        self.buttons = []

        for index in range(9):
            button = tk.Button(
                root,
                text="",
                width=8,
                height=3,
                font=("Arial", 20, "bold"),
                command=lambda position=index: self.handle_click(position),
            )
            button.grid(row=(index // 3) + 1, column=index % 3, padx=4, pady=4)
            self.buttons.append(button)

        self.new_game_button = tk.Button(
            root,
            text="New game",
            font=("Arial", 12),
            command=self.start_new_game,
        )
        self.new_game_button.grid(row=4, column=0, columnspan=3, pady=10)

        self.start_new_game()

    def start_new_game(self):
        self.board = initialize_board()
        self.game_over = False

        self.human_player = random.choice([X_PLAYER, O_PLAYER])
        self.computer_player = O_PLAYER if self.human_player == X_PLAYER else X_PLAYER
        self.current_player = X_PLAYER

        for button in self.buttons:
            button.config(text="", state=tk.NORMAL)

        self.status_label.config(
            text=f"Aap {self.human_player} ke roop me khelenge. "
                 f"Computer {self.computer_player} ke roop me khelega."
        )

        if self.current_player == self.computer_player:
            self.root.after(500, self.make_computer_move)
        else:
            self.status_label.config(
                text=f"Aap {self.human_player} ke roop me khelenge. Aapki turn."
            )

    def handle_click(self, position):
        if self.game_over:
            return

        if self.current_player != self.human_player:
            return

        if self.board[position] != EMPTY_SPOT:
            messagebox.showwarning(
                "Invalid move",
                "Ye space already occupied hai.",
            )
            return

        self.make_move(position, self.human_player)

        if not self.game_over:
            self.current_player = self.computer_player
            self.status_label.config(text="Computer ki turn...")
            self.root.after(500, self.make_computer_move)

    def make_computer_move(self):
        if self.game_over:
            return

        move = get_rules_based_ai_move(self.computer_player, self.board)

        if move is not None:
            self.make_move(move, self.computer_player)

        if not self.game_over:
            self.current_player = self.human_player
            self.status_label.config(text="Aapki turn.")

    def make_move(self, position, player):
        self.board[position] = player
        self.buttons[position].config(text=player, state=tk.DISABLED)

        winner = check_winner(self.board)

        if winner:
            self.game_over = True
            self.disable_board()

            if winner == self.human_player:
                self.status_label.config(text="Aap jeet gaye!")
                messagebox.showinfo("Game over", "Badhaai ho! Aap game jeet gaye.")
            else:
                self.status_label.config(text="Computer jeet gaya.")
                messagebox.showinfo("Game over", "Computer ye game jeet gaya.")

            return

        if check_draw(self.board):
            self.game_over = True
            self.disable_board()
            self.status_label.config(text="Draw.")
            messagebox.showinfo("Game over", "Game draw ho gaya.")

    def disable_board(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
