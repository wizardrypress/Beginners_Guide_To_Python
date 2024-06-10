import tkinter as tk



def on_click(event=None):
    print("Button was clicked!")


root = tk.Tk()
root.title("My First Tkinter Application")

button = tk.Button(root, text="Click Me")
button.pack()

button.bind("<Button-1>", on_click)  # Bind left mouse click to on_click

root.mainloop()
