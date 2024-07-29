'''
@Author: v sanjay kumar
@Date: 2024-07-26 11:24:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-26 11:24:30
@Title :n program to add 'ing' at the end of a given string (length should be at
        least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
         given string is less than 3, leave it unchanged.

'''


def ing_all(given_string):
    """
    descripton
      function to change the first leter to occure in a string replace with $ and did not change the first latter .

    Parameters:
    - given_string (set):string is  user given.

    Returns:
    - dict -Return the new string which satisfy all conditions.
    """
    if len(given_string) < 3:
        return f"The length should be greater than 3: {given_string}"
    elif given_string[-3:] == "ing":
        new_string = given_string + "ly"
    else:
        new_string = given_string + "ing"
    
    return new_string
    
def main():
    string = input("Enter a string : ")
    
    print("The final resulten string is:",ing_all(string))

if __name__ =="__main__":
    main()