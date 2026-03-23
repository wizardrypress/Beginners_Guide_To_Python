import tkinter as tk

def show_address():
    address = text_box.get("1.0", tk.END).strip()
    print(f"Address entered: {address}")

root = tk.Tk()
root.title("Text Widget Example")

label = tk.Label(root, text="Enter your address:", font=('Arial', 14))
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

text_box = tk.Text(root, height=5, width=40, font=('Arial', 14), bg="lightyellow")
text_box.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Submit", command=show_address, font=('Arial', 14))
button.grid(row=1, column=0, columnspan=2, pady=10)

# Insert a humorous example address into the text box
example_address = "123 Python Road\nCode City, PY 12345\nPlanet Earth"
text_box.insert(tk.END, example_address)

root.mainloop()
