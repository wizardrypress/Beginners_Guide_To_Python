import tkinter as tk
from tkinter import messagebox


def ask_yes_no():
    answer = messagebox.askyesno(
        "Confirmation",
        "Kya aap continue karna chahte hain?",
        icon="question",
        default="no",
    )

    if answer:
        messagebox.showinfo("Answer", "Aapne Yes choose kiya.")
    else:
        messagebox.showinfo("Answer", "Aapne No choose kiya.")


root = tk.Tk()
root.withdraw()

ask_yes_no()

root.mainloop()
