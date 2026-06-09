import tkinter as tk
from tkinter import messagebox


def mostrar_error():
    messagebox.showerror(
        "Error",
        "Humor no encontrado. Revisa la configuración de tus chistes.",
        icon="error",
    )


root = tk.Tk()
root.withdraw()

mostrar_error()

root.mainloop()
