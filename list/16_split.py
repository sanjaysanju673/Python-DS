'''
@Author: v sanjay kumar
@Date: 2024-07-25 12:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 12:30:30.
@Title : Python program to split a list based on the first character of word.
'''

def split_list_by_first_char(words):
    '''
    Splits a list of words based on the first character of each word.

    Parameters:
    - words (list): The list of words.

    Returns:
    - dict: A dictionary where the keys are the first characters, and the values are lists of words starting with that character.
    '''
    split_dict = {}
    
    for word in words:
        if word:
            first_char = word[0].lower()  # Convert to lowercase for case-insensitivity
            if first_char not in split_dict:
                split_dict[first_char] = []
            split_dict[first_char].append(word)
    
    return split_dict

def main():
    words_list = ["apple", "banana", "apricot", "cherry", "blueberry", "cranberry", "avocado"]
    
    result = split_list_by_first_char(words_list)
    print("The split list based on the first character of each word:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
