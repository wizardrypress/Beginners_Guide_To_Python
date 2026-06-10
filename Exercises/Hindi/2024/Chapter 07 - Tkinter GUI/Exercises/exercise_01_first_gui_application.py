import tkinter as tk


root = tk.Tk()
root.title("Meri pehli Tkinter application")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=10)


def on_click():
    label.config(text="Button press ho gaya!")


button = tk.Button(root, text="Click karo", command=on_click)
button.pack(pady=10)

root.mainloop()
