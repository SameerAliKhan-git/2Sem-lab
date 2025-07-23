# Write a program with a function that accepts a string as an argument and returns the number of vowels that the string contains. Another function to return the number of consonants.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# Example usage:
text = input("Enter a string: ")

print(f"Number of vowels: {count_vowels(text)}")
print(f"Number of consonants: {count_consonants(text)}")



