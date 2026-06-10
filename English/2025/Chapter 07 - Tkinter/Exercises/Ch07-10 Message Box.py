import tkinter as tk
from tkinter import messagebox

def show_error():
    messagebox.showerror("Error",
                         "Humor Not Found. Please check your joke settings.",
                         icon='error')


root = tk.Tk()
root.withdraw()  # Hide the root window

show_error()

root.mainloop()
