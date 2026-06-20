import tkinter as tk

def button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Button Widget Example")

button = tk.Button(root, text="Click Me", command=button_click, bg="lightblue", font=('Arial', 14))
button.pack(pady=10)

root.mainloop()
