# 
# 04. Write recursive and non-recursive functions for the following: 
    # a) Tower of Hanoi 
    # b) To find GCD of two integers. 
    # c) To find the factorial of a positive integer. 
    # d) To print Fibonacci series up to a given number n. 

# Recursive Solution

def hanoi_recursive(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi_recursive(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    hanoi_recursive(n-1, auxiliary, source, target)



hanoi_recursive(3, "A", "B", "C")