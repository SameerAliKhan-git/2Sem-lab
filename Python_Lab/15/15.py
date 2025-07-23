#  Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures. 

import tkinter as tk

def convert():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = celsius * 9/5 + 32
        label_result.config(text=f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
    except ValueError:
        tk.messagebox.showerror("Invalid input", "Please enter a valid number.")

# Set up the GUI window
root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")

# Celsius input
tk.Label(root, text="Celsius:").grid(row=0, column=0, padx=10, pady=10)
entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.grid(row=1, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Fahrenheit: --")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
