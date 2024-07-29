'''
    @Author: v sanjay kumar
    @Date: 2024-07-26 03:24:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-26 03:24:30
    @Title : program to get the last part of a string before a specified character.

'''



def display_last(user_input):
    """
    Description:
    Function that takes a user input string and returns last part of string before a specified character.

    Parameters:
    - user_input (str): The user-given string.

    Returns:
    - str:last part of string before a specified character.
    """
    last_part = (user_input.rsplit("-",1))[0]
    return last_part



def main():
    user_input = input("Enter a string: ")
    
    print("the last part of a string before a specified character", display_last(user_input))



if __name__ == "__main__":
    main()
