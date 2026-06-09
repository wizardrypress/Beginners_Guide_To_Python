import tkinter as tk
from tkinter import messagebox


def agregar_tarea():
    tarea = entry.get()

    if tarea != "":
        tasks_listbox.insert(tk.END, tarea)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")


def eliminar_tarea():
    try:
        task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminar.")


root = tk.Tk()
root.title("Lista de tareas")

frame = tk.Frame(root)
frame.pack(pady=10)

tasks_listbox = tk.Listbox(frame, width=50, height=10, bd=0)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

add_button = tk.Button(root, text="Agregar tarea", command=agregar_tarea)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar tarea", command=eliminar_tarea)
delete_button.pack(pady=5)

root.mainloop()
