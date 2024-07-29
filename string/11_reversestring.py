'''
    @Author: v sanjay kumar
    @Date: 2024-07-26 03:24:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-26 03:24:30
    @Title : program to reverse a string.

'''



def reverse_string(User_input):
    """
    Description:
    Function that takes a text string and returns reverse of string .

    Parameters:
    - string (str): The text string to be formatted.
   

    Returns:
    - str: reverse of  substring.
    """
    rev =''
    for i in User_input:
        rev =i+rev
    

    return rev 

def main():
    user_input= input("Enter the main string: ")
   

    print("reverse of substrig",reverse_string(user_input))

if __name__ == "__main__":
    main()
