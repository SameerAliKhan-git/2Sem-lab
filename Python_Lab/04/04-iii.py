# b) GCD (Greatest Common Divisor) of Two Integers

# Recursive Solution
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# Example usage
a = 48
b = 18  
print(f"GCD of {a} and {b} is {gcd_recursive(a, b)}")