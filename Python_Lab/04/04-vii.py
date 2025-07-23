# d) Fibonacci Series up to n Terms
# Recursive Solution
def fibonacci_recursive(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seq = fibonacci_recursive(n-1)
    seq.append(seq[-1] + seq[-2])
    return seq

# Print sequence
n = 7
print(fibonacci_recursive(n))



