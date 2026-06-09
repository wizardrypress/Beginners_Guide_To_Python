import tkinter as tk


root = tk.Tk()
root.title("Mi primera aplicación con Tkinter")

label = tk.Label(root, text="¡Hola, Tkinter!", font=("Arial", 14))
label.pack(pady=10)


def al_hacer_clic():
    label.config(text="¡Botón presionado!")


button = tk.Button(root, text="Haz clic", command=al_hacer_clic)
button.pack(pady=10)

root.mainloop()
