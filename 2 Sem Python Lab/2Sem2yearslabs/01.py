def find_Area(r):
    pi = 3.142
    area = pi * r * r
    return area

# This function calculates the area of a circle given its radius.

if __name__ == "__main__":
    radius = 10
    area = find_Area(radius)
    print(f"The area of the circle with radius {radius} is: {area:.10f}")