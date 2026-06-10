import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Example")

label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2)

root.mainloop()
