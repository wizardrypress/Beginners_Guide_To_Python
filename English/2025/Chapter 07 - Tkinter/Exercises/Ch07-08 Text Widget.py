import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}")

root = tk.Tk()
root.title("Frame Widget Example")

frame = tk.Frame(root, relief=tk.RAISED, borderwidth=2)
frame.pack(padx=10, pady=10)

name_label = tk.Label(frame, text="Name:", font=('Arial', 14))
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(frame, width=30, font=('Arial', 14))
name_entry.grid(row=0, column=1, padx=5, pady=5)

email_label = tk.Label(frame, text="Email:", font=('Arial', 14))
email_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(frame, width=30, font=('Arial', 14))
email_entry.grid(row=1, column=1, padx=5, pady=5)

submit_button = tk.Button(frame, text="Submit", command=submit_form, font=('Arial', 14))
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
