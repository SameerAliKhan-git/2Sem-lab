"""
Write a program with a text entry box and a button. When the button is clicked, the text from the entry box should be displayed in a label.
"""

import tkinter as tk
# Import the themed widget set
from tkinter import ttk

def display_text():
    """
    Gets text from the entry box and displays it in the result label.
    """
    input_text = entry.get()
    # Check if the input is empty to avoid displaying an empty message
    if input_text:
        label_result.config(text=f"You entered: {input_text}")
    else:
        label_result.config(text="Please enter some text.")

# --- Main Application Window ---
root = tk.Tk()
root.title("Text Display App")
root.geometry("400x200")
root.resizable(False, False) # Optional: make the window not resizable

# Configure the grid to have padding and make the frame expand
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# --- Main Frame ---
# Create a frame to hold all the content
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew") # The frame will fill the window

# --- Widgets ---

# Entry widget for user input
entry = ttk.Entry(main_frame, width=40, font=("Helvetica", 12))
entry.grid(row=0, column=0, columnspan=2, pady=(0, 10))
# Set focus on the entry widget so the user can start typing immediately
entry.focus()

# Button to trigger the display
btn_show = ttk.Button(main_frame, text="Display Text", command=display_text)
btn_show.grid(row=1, column=0, columnspan=2, pady=5)

# Label to show the result
label_result = ttk.Label(main_frame, text="", font=("Helvetica", 12, "italic"), foreground="navy")
label_result.grid(row=2, column=0, columnspan=2, pady=(10, 0))

# --- Run the Application ---
root.mainloop()