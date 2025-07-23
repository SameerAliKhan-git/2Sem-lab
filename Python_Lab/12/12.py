#  Create a program with a calculator class with methods of basic arithmetic operations.  


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

# --- Main Program ---
def main():
    calc = Calculator()

    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    print("\nResults:")
    print(f"Addition: {calc.add(a, b)}")
    print(f"Subtraction: {calc.subtract(a, b)}")
    print(f"Multiplication: {calc.multiply(a, b)}")
    print(f"Division: {calc.divide(a, b)}")

if __name__ == "__main__":
    main()



