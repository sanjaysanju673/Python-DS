def display_cases(user_input):
    """
    Description:
    Function that takes a user input string and returns it in both upper and lower cases.

    Parameters:
    - user_input (str): The user-given string.

    Returns:
    - tuple: A tuple containing the input string in upper and lower cases.
    """
    upper_case = user_input.upper()
    lower_case = user_input.lower()
    return upper_case, lower_case

def main():
    user_input = input("Enter a string: ")
    upper_case, lower_case = display_cases(user_input)
    print("Upper case:", upper_case)
    print("Lower case:", lower_case)

if __name__ == "__main__":
    main()
