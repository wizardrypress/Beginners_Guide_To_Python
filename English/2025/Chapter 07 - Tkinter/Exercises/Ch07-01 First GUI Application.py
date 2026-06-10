import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter Application")

label = tk.Label(root, text="Hello, Tkinter!", font=('Arial', 14))
label.pack(pady=10)

def on_button_click():
    label.config(text="Button clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()