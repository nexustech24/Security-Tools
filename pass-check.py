import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength(password):
    reasons = []

    if len(password) < 8:
        reasons.append("it is less than 8 characters long.")
    if not re.search("[a-z]", password):
        reasons.append("it does not contain any lowercase letters.")
    if not re.search("[A-Z]", password):
        reasons.append("it does not contain any uppercase letters.")
    if not re.search("[0-9]", password):
        reasons.append("it does not contain any digits.")
    if not re.search("[@#$%^&*()_+!]", password):
        reasons.append("it does not contain any special characters (@#$%^&*()_+!).")

    if not reasons:
        return "Your password is strong because it meets all the criteria."
    else:
        return "Your password is weak because " + " ".join(reasons)

# Function to handle the button click
def on_check_button_click():
    password = password_entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
tk.Label(root, text="Enter your password:").pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_check.pack()

check_button = tk.Button(root, text="Check Password Strength", command=on_check_button_click)
check_button.pack(pady=20)

# Run the application
root.mainloop()
