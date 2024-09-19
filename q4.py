# Write a python GUI program to generate a random password with upper and lower case letters
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    """Generate a random password of the given length."""
    if length < 1:
        messagebox.showerror("Error", "Length must be at least 1")
        return ""
    
    # Create a pool of characters: uppercase and lowercase letters
    characters = string.ascii_letters  # includes both a-z and A-Z
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def on_generate():
    """Handle the generate button click."""
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_entry.delete(0, tk.END)  # Clear previous password
        password_entry.insert(0, password)  # Insert new password
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for length.")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

# Password label and entry
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Run the application
root.mainloop()
