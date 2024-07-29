'''
    @Author: v sanjay kumar
    @Date: 2024-07-26 02:24:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-26 02:24:30
    @Title :program that takes a list of words and returns the length of the longest one.

'''


def ing_all(given_string):
    """
    descripton
      function to that takes a list of words and returns the length of the longest one .

    Parameters:
    - given_string (set):string is  user given.

    Returns:
    - str -Return the longest word.
    """
    old_string =list(given_string.split())
    long_word =old_string[0]
    for i in old_string:
        if len(long_word) < len(i):
            long_word = i
        
    return long_word



def main():
    string = input("Enter a string with spaces : ")
    
    print("The final resulten string is:",ing_all(string))

if __name__ =="__main__":
    main()