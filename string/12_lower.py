'''
@Author: v sanjay kumar
@Date: 2024-07-28 14:00:00
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-28 14:00:00
@Title: Program to lowercase the first n characters in a string.
'''

def lowercase_first_n(user_input, n):
    """
    Description:
    Function that takes a text string and lowercases the first n characters.

    Parameters:
    - user_input (str): The text string to be modified.
    - n (int): The number of characters to lowercase.

    Returns:
    - str: Modified string with the first n characters lowercased.
    """
    return user_input[:n].lower() + user_input[n:]

def main():
    user_input = input("Enter the main string: ")
    n = int(input("Enter the number of characters to lowercase: "))
    print("Modified string:", lowercase_first_n(user_input, n))

if __name__ == "__main__":
    main()
