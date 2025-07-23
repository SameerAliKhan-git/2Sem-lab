# Write a Python program, write a function that accepts two arguments: a list and a number n. The function displays all of the numbers in the list that are greater than the number n. 
def display_greater_than(lst, n):
    """
    Displays all numbers in lst greater than n.
    """
    for num in lst:
        if num > n:
            print(num)
# Example list and value
numbers = [8, 3, 10, 1, 6, 15, 7]
n = 6

print(f"Numbers greater than {n}:")
display_greater_than(numbers, n)
