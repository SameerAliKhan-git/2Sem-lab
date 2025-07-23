# 
# 04. Write recursive and non-recursive functions for the following: 
    # a) Tower of Hanoi 
    # b) To find GCD of two integers. 
    # c) To find the factorial of a positive integer. 
    # d) To print Fibonacci series up to a given number n. 

# Non-Recursive Solution
def hanoi_non_recursive(n, source, auxiliary, target):
    total_moves = 2 ** n - 1
    rods = {source: [], auxiliary: [], target: []}
    for i in range(n, 0, -1):
        rods[source].append(i)
    names = [source, auxiliary, target] if n % 2 == 1 else [source, target, auxiliary]

    for move in range(1, total_moves + 1):
        from_rod = names[(move & move - 1) % 3]
        to_rod = names[((move | move - 1) + 1) % 3]
        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        print(f"Move disk {disk} from {from_rod} to {to_rod}")

hanoi_non_recursive(3, "A", "B", "C")
