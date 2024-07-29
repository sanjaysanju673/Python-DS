'''
    @Author: v sanjay kumar
    @Date: 2024-07-26 03:24:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-26 03:24:30
    @Title :program to display formatted text (width=50) as output.

'''



import textwrap

def format_text(text, width=50):
    """
    Description:
    Function that takes a text string and returns it formatted with a specified width.

    Parameters:
    - text (str): The text string to be formatted.
    - width (int): The width for formatting the text.

    Returns:
    - str: The formatted text.
    """
    formatted_text = textwrap.fill(text, width=width)
    return formatted_text

def main():
    text = input("Enter the text to be formatted: ")
    print("Formatted text with width 50:\n")
    print(format_text(text))

if __name__ == "__main__":
    main()
