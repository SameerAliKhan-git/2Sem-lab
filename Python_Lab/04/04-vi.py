# c) Factorial of a Positive Integer
# Non-Recursive Solution
def factorial_non_recursive(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = 5 
print(f"Factorial of {n} is {factorial_non_recursive(n)}")

