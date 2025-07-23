# Write a program to implement inheritance: 
# a) Method overloading 
# b) Method overriding.

# a) Method Overloading Example
class Display:
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Two arguments: {a} and {b}")
        elif a is not None:
            print(f"One argument: {a}")
        else:
            print("No arguments")

# Usage
disp = Display()
disp.show()
disp.show(5)
disp.show(5, 10)




