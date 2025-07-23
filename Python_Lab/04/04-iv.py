# b) GCD (Greatest Common Divisor) of Two Integers

# Non-Recursive Solution
def gcd_non_recursive(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Non-Recursive Test
print("Non-Recursive GCD of 48 and 18:", gcd_non_recursive(48, 18))


