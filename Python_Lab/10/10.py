# Write a program to analyze the contents of two text files using set operations.  


def get_unique_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        # Replace punctuation with spaces and convert to lowercase
        for ch in ",.!?-;:\'\"()[]{}":
            text = text.replace(ch, " ")

        words = text.lower().split()
        return set(words)

    except FileNotFoundError:
        print(f" Error: File '{filename}' not found.")
        return set()

def analyze_files(file1, file2):
    words1 = get_unique_words(file1)
    words2 = get_unique_words(file2)

    print(f"\nAnalyzing files: '{file1}' and '{file2}'\n")

    print(f" Total unique words in {file1}: {len(words1)}")
    print(f" Total unique words in {file2}: {len(words2)}")

    print("\n Words common in both files (intersection):")
    print(words1 & words2)

    print("\n Words unique to first file (difference):")
    print(words1 - words2)

    print("\n Words unique to second file (difference):")
    print(words2 - words1)

    print("\n All unique words from both files (union):")
    print(words1 | words2)

    print("\n Words present in only one file (symmetric difference):")
    print(words1 ^ words2)

# --- Usage Example ---
file1 = input("Enter the first file name (e.g., file1.txt): ")
file2 = input("Enter the second file name (e.g., file2.txt): ")

analyze_files(file1, file2)
