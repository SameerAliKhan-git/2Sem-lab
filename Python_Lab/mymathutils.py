# mymathutils.py

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]