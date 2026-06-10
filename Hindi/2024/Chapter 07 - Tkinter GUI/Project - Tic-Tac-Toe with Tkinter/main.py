import tkinter as tk

from game_gui import TicTacToeApp


def main():
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
