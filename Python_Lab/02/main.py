# 02. Write a Python program using a user-defined Python module which includes a prime number checking function with a palindrome function.


# main.py

import mymathutils

def main():
    num = int(input("Enter a number: "))
    
    # Check if the number is prime
    if mymathutils.is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

    # Check if the number is a palindrome
    if mymathutils.is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
if __name__ == "__main__":
    main()
