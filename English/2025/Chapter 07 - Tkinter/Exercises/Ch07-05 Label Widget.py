import tkinter as tk

root = tk.Tk()
root.title("Label Widget Example")

label = tk.Label(root, text="This is a label", font=('Arial', 14), bg="yellow")
label.pack(pady=10)

root.mainloop()
