import tkinter as tk


root = tk.Tk()
root.title("Grid layout example")

label_1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label_2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label_3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

label_1.grid(row=0, column=0)
label_2.grid(row=1, column=1)
label_3.grid(row=2, column=2)

root.mainloop()
