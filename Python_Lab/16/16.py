# Write a GUI program using Tkinter that displays your details when a button is clicked.

import tkinter as tk

def show_details():
    details = (
        "Name: Sameer Ali Khan\n"
        "Age: 23\n"
        "Email: sammysameerkhan007@gmail.com\n"
        "Occupation: Student"
    )
    label_output.config(text=details)

root = tk.Tk()
root.title("Display Your Details")
root.geometry("350x250")  # Increased height

heading = tk.Label(root, text="Click to View Details", font=("Arial", 18))
heading.pack(pady=10)

btn_show = tk.Button(root, text="Show Details", command=show_details)
btn_show.pack(pady=5)

label_output = tk.Label(root, text="", font=("Arial", 10), justify="left", width=40, height=6, anchor="nw")
label_output.pack(pady=10)

root.mainloop()


