# c) Factorial of a Positive Integer
# Recursive Solution
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)


n = 5
print(f"Factorial of {n} (recursive): {factorial_recursive(n)}")
