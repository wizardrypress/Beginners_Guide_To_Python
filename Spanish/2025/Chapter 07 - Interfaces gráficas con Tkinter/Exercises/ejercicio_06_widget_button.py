import tkinter as tk


def boton_presionado():
    print("¡Botón presionado!")


root = tk.Tk()
root.title("Ejemplo del widget Button")

button = tk.Button(
    root,
    text="Haz clic",
    command=boton_presionado,
    bg="lightblue",
    font=("Arial", 14),
)
button.pack(pady=10)

root.mainloop()
