import tkinter as tk


root = tk.Tk()
root.title("Place layout example")

label_1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label_2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label_3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

label_1.place(x=50, y=50)
label_2.place(x=100, y=100)
label_3.place(x=150, y=150)

root.mainloop()
