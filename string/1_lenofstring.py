'''

    @Author: v sanjay kumar
    @Date: 2024-07-26 11:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-26 11:00:30
    @Title :find the length of the string.

'''


def len_string(string):
    """
    Description:
        find the given string length.

    Parameters:
        string (str):given string.

    Returns:
        int: return length of the string.
    """
    length =0
    print(len(string))
    for i in string:
        length =length +1
    
    return length

def main():
    string = input("Enter a string to find length :")
    print("Given string length :",len_string(string))


if __name__ == "__main__":
    main()