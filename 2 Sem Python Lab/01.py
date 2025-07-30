def find_Area(r):
    """Calculates the area of a circle."""
    PI = 3.142
    return PI * (r * r)

#Driver code
if __name__ == "__main__":
    print(f"Area of circle with radius 10 is: {find_Area(10):.6f}")