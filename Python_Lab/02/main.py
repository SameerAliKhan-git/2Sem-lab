# 02. Write a Python program using a user-defined Python module which includes a prime number checking function with a palindrome function.


# main.py

import sys
import mymathutils

def main():
    try:
        # Check if a command-line argument was provided
        if len(sys.argv) < 2:
            print("Usage: python main.py <number>")
            # Exit gracefully if no number is given
            return

        num_input = sys.argv[1] # Get the number from the command line
        num = int(num_input)
        
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
    except ValueError:
        print(f"Invalid input. '{num_input}' is not a valid integer.")

if __name__ == "__main__":
    main()
