import tkinter as tk


def evaluar_expresion(expresion):
    try:
        return eval(expresion)
    except Exception:
        return "Error"


def al_hacer_clic(caracter):
    if caracter == "=":
        resultado = evaluar_expresion(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    elif caracter == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, caracter)


root = tk.Tk()
root.title("Calculadora simple")

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+",
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: al_hacer_clic(x)
    tk.Button(root, text=button, width=10, height=2, command=action).grid(
        row=row_val,
        column=col_val,
    )

    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
