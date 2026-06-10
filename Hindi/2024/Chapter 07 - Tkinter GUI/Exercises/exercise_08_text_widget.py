import tkinter as tk


def show_address():
    address = text_box.get("1.0", tk.END).strip()
    print(f"Entered address: {address}")


root = tk.Tk()
root.title("Text widget example")

label = tk.Label(root, text="Apna address enter karo:", font=("Arial", 14))
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

text_box = tk.Text(root, height=5, width=40, font=("Arial", 14), bg="lightyellow")
text_box.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Submit", command=show_address, font=("Arial", 14))
button.grid(row=1, column=0, columnspan=2, pady=10)

example_address = "123 Python Street\nCode City, PY 12345\nEarth"
text_box.insert(tk.END, example_address)

root.mainloop()
