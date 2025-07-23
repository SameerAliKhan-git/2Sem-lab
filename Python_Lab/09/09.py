# Write a program that opens a specified text file and then displays a list of all the unique words found in the file. (Store each word as an element of a set.) 

def extract_unique_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Remove punctuation and make lowercase
        for ch in ",.!?-;:\'\"()[]{}":
            text = text.replace(ch, " ")

        words = text.lower().split()
        unique_words = set(words)

        print(f"\nUnique words in '{file_path}':")
        for word in sorted(unique_words):
            print(word)

    except FileNotFoundError:
        print(f" Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- Example usage ---
filename = input("Enter the text file name (e.g., sample.txt): ")
extract_unique_words(filename)

