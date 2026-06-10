import tkinter as tk


def button_pressed():
    print("Button press ho gaya!")


root = tk.Tk()
root.title("Button widget example")

button = tk.Button(
    root,
    text="Click karo",
    command=button_pressed,
    bg="lightblue",
    font=("Arial", 14),
)
button.pack(pady=10)

root.mainloop()
