import tkinter as tk


root = tk.Tk()
root.title("Ejemplo del widget Label")

label = tk.Label(
    root,
    text="Esto es una etiqueta",
    font=("Arial", 14),
    bg="yellow",
)
label.pack(pady=10)

root.mainloop()
