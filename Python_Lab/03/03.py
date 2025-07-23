# 03. Write a program to demonstrate global variables, global constants, and local variables. 

# Global constant (by convention, uppercase)
PI = 3.14159

# Global variable
radius = 10

def calculate_area():
    # Local variable
    area = PI * radius * radius
    print(f"Area of circle: {area}")

def update_radius(new_radius):
    global radius   # Declare we are using the global variable
    radius = new_radius
    print(f"Updated global radius to: {radius}")

def display_variables():
    # Local variable
    local_message = "Local scope demonstration"
    print(f"PI (Global Constant): {PI}")
    print(f"radius (Global Variable): {radius}")
    print(f"local_message (Local Variable): {local_message}")

# --- Main Program ---

calculate_area()           # Uses global radius
update_radius(5)           # Updates global radius
calculate_area()           # Now uses updated radius
display_variables()



