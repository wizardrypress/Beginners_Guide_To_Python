import tkinter as tk
from tkinter import messagebox


def ask_yes_no():
    response = messagebox.askyesno("Confirmation", "Do you want to proceed?", icon='question', default='no')
    if response:
        messagebox.showinfo("Response", "You chose Yes!")
    else:
        messagebox.showinfo("Response", "You chose No!")


root = tk.Tk()
root.withdraw()  # Hide the root window

ask_yes_no()

root.mainloop()
