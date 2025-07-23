# d) Fibonacci Series up to n Terms
# Non-Recursive 

def fibonacci_non_recursive(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Print sequence
n = 7
print(fibonacci_non_recursive(n))



