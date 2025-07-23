# Write a Python program which takes command line arguments as input. Then, using one print function, print the arguments using a separator and store those in a file. 


import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py arg1 arg2 ...")
        return
    
    separator = ", "
    args = sys.argv[1:]
    output_file = "output.txt"
    
    # Construct output string
    output_str = separator.join(args)
    
    # Print to screen and save to file
    with open(output_file, "w") as file:
        print(output_str, file=file)
    print(output_str)  # Print to console

if __name__ == "__main__":
    main()



