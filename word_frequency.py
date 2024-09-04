"""
The code for this exercise was copied from the Udemy course "Learn Python
by coding 10 mini projects". The work I did was the homework: allowing
user to input via file instead of text.
"""

# 1. Import the necessary functionality
from collections import Counter
import re


# 2. Create a function for getting the word frequency in text
def get_frequency(text: str) -> list[tuple[str, int]]:
    # 3. Convert text to lowercase to ensure case-insensitivity
    lowered_text: str = text.lower()

    # 4. Use regular expression to find all words (alphanumeric and underscore)
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)

    # 5. Count word frequencies using Counter
    word_counts: Counter = Counter(words)

    # 6. Return the most common words as a tuple
    return word_counts.most_common(3)


# 7. Create a main entry point
def main() -> None:
    # 8. Get that user input
    while True:
        insert_file = input("Would you like to type your text or open a file? (type/file) ").strip().lower()
        if insert_file in ["type", "file"]:
            break
        else:
            print("Please enter 'type' or 'file' to continue.")
    
    if insert_file == "type":
        text: str = input('Enteryour text: ')
    
    if insert_file == "file":
        file = input("Make sure your file is in this directory. What is the file name? ")
        with open(file, 'r') as my_file:
            text = my_file.read().strip()

    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    # 9. Display the results
    for word, count in word_frequencies:
        print(f'{word}: {count}')


# 10. Run the script
if __name__ == "__main__":
    main()