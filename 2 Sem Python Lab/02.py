"""
2.Write a python program which takes command line arguments as input. Then, 
using one print function, print the arguments using a seperator and store those 
in a file.
"""

# import sys
# # Ensure the length of sys.argv is at least 1
# n = len(sys.argv)
# # Create a copy of sys.argv for modification, if needed
# args = sys.argv[:]
# args[0] = ""
# # Define the file path using raw string
# file_path = r"Python_program_to_find_Area_of_a.txt"
# try:
#  # Open the file in write mode
#     with open(file_path, "w") as f:
#  # Print arguments to standard output
#         print("The arguments passed are")
#         print(*args, sep=' ', end='.', file=sys.stdout, flush=False)
#     # Print arguments to the file
#         print(*args, sep=' ', end='.', file=f, flush=False)
# except IOError as e:
#     print(f"An error occurred while writing to the file: {e}")


# Python program to demonstrate
# command line arguments


import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
    
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
    
print("\n\nResult:", Sum)