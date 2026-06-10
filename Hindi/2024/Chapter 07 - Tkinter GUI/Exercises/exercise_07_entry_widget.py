import tkinter as tk


root = tk.Tk()
root.title("Entry widget example")

label = tk.Label(root, text="Apna naam enter karo:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

root.mainloop()
