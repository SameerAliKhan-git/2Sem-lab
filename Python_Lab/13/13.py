# Write a program to implement inheritance and dynamic polymorphism.

class Shape:
    def area(self):
        # Base method, to be overridden by subclasses
        print("Calculating area in Shape (should be overridden).")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Rectangle area: {self.width * self.height}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Circle area: {3.14159 * self.radius * self.radius}")

# Demonstration of dynamic polymorphism
shapes = [
    Rectangle(3, 4),
    Circle(2),
    Rectangle(5, 6),
    Circle(5)
]

for shape in shapes:
    shape.area()  # The correct area() for the object's real class is called



