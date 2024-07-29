'''
    @Author: v sanjay kumar
    @Date: 2024-07-26 03:24:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-26 03:24:30
    @Title : program to count occurrences of a substring in a string.

'''



def substring_count(User_input,substring):
    """
    Description:
    Function that takes a text string and returns it substring count.

    Parameters:
    - string (str): The text string to be formatted.
    - substring  (str): user given substring.

    Returns:
    - int: count of substring.
    """
    return User_input.count(substring)

def main():
    user_input= input("Enter the main string: ")
    substring = input("Enter the substring")

    print("count of substrig",substring_count(user_input,substring))

if __name__ == "__main__":
    main()
