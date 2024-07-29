"""
@Author: v sanjay kumar
@Date: 2024-07-27
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-27
@Title: Program that accepts a comma-separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
"""

def get_unique_sorted_words(input_sequence):
    """
    Description:
    Function that takes a comma-separated sequence of words and returns the unique words in sorted order.

    Parameters:
    - input_sequence (str): The user-given comma-separated string of words.

    Returns:
    - list: A list of unique words sorted alphanumerically.
    """
    words = input_sequence.split(',')
    unique_words = sorted(set(word.strip() for word in words))
    return unique_words

def main():
    user_input = input("Enter a comma-separated sequence of words: ")
    sorted_unique_words = get_unique_sorted_words(user_input)
    print("Unique sorted words:", ", ".join(sorted_unique_words))

if __name__ == "__main__":
    main()
