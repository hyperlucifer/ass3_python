# Write Python GUI program to add menu bar with name of colors as 
# options to change the background color as per selection from menu option.

import tkinter as tk
from tkinter import Menu

def change_background(color):
    """Change the background color of the main window."""
    root.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Color Changer")

# Create a menu bar
menu_bar = Menu(root)

# Define color options
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Pink', 'White', 'Black']

# Add color options to the menu
color_menu = Menu(menu_bar, tearoff=0)
for color in colors:
    color_menu.add_command(label=color, command=lambda c=color: change_background(c.lower()))

menu_bar.add_cascade(label="Colors", menu=color_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Set the default background color
root.config(bg="white")

# Run the application
root.mainloop()
