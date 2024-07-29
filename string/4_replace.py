'''
@Author: v sanjay kumar
@Date: 2024-07-24 11:24:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 11:24:30
@Title :program to get a string from a given string where all occurrences of its
         first char have been changed to '$', except the first char itself.

'''


def Replace_all(given_string):
    """
    descripton
      function to change the first leter to occure in a string replace with $ and did not change the first latter .

    Parameters:
    - given_string (set):string is  user given.

    Returns:
    - dict -Return the new string which satisfy all conditions.
    """
    new_string =  given_string[0]
    for i in range(1,len(given_string)):
        if given_string[0] ==given_string[i]:
            new_string  += "&"
        else:
            new_string += given_string[i]
    return new_string       
            
   
    
def main():
    string = input("Enter a string : ")
    
    print("The final resulten string is:",Replace_all(string))

if __name__ =="__main__":
    main()