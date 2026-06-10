import tkinter as tk
from tkinter import messagebox


def show_error():
    messagebox.showerror(
        "Error",
        "Setting check karo. Example error message yahan dikh raha hai.",
        icon="error",
    )


root = tk.Tk()
root.withdraw()

show_error()

root.mainloop()
