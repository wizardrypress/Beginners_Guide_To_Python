import tkinter as tk
from tkinter import messagebox


def preguntar_si_no():
    respuesta = messagebox.askyesno(
        "Confirmación",
        "¿Quieres continuar?",
        icon="question",
        default="no",
    )

    if respuesta:
        messagebox.showinfo("Respuesta", "Elegiste Sí.")
    else:
        messagebox.showinfo("Respuesta", "Elegiste No.")


root = tk.Tk()
root.withdraw()

preguntar_si_no()

root.mainloop()
