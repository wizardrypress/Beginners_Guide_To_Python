import tkinter as tk


def mostrar_direccion():
    direccion = text_box.get("1.0", tk.END).strip()
    print(f"Dirección ingresada: {direccion}")


root = tk.Tk()
root.title("Ejemplo del widget Text")

label = tk.Label(root, text="Ingresa tu dirección:", font=("Arial", 14))
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

text_box = tk.Text(root, height=5, width=40, font=("Arial", 14), bg="lightyellow")
text_box.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Enviar", command=mostrar_direccion, font=("Arial", 14))
button.grid(row=1, column=0, columnspan=2, pady=10)

direccion_ejemplo = "123 Calle Python\nCiudad Código, PY 12345\nPlaneta Tierra"
text_box.insert(tk.END, direccion_ejemplo)

root.mainloop()
