import tkinter as tk


root = tk.Tk()
root.title("Label widget example")

label = tk.Label(
    root,
    text="Ye ek label hai",
    font=("Arial", 14),
    bg="yellow",
)
label.pack(pady=10)

root.mainloop()
