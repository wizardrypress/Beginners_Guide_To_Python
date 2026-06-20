import tkinter as tk

root = tk.Tk()
root.title("Pack Layout Example")

label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

label1.pack(side="top", fill="x")
label2.pack(side="left", fill="y")
label3.pack(side="bottom", fill="x")

root.mainloop()