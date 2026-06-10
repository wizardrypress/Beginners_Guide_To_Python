import tkinter as tk


root = tk.Tk()
root.title("Pack layout example")

label_1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label_2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label_3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

label_1.pack(side="top", fill="x")
label_2.pack(side="left", fill="y")
label_3.pack(side="bottom", fill="x")

root.mainloop()
