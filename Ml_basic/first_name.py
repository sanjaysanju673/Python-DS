'''
@Author: v sanjay kumar
@Date: 2024-07-18 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 10:00:30
@Title :print first name and last name
'''
def first_name(first_name ,last_name):
    """
    it is accepts the user's first and last name and print them in
    reverse order with a space between them.

    Parameters:
    First_name (str): first name.
    last_name(list):last name.

    Returns:
    str: it return the user's first and last name and print them in
    reverse order with a space between them
    """
    return f"{first_name[::-1]}  {last_name[::-1]}"


def main():
    first_n = input(" Enter your first name :")
    last_name = input("Enter  your second name :")
    print(first_name(first_n,last_name))

if __name__ == "__main__":
    main()