'''
@Author: v sanjay kumar
@Date: 2024-07-22 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 11:30:30
@Title :unique elements
'''

def check(a_set,b_set):
    '''the function takes the  two tupples  and    returns  unique values.

    Parameters:
    a_set(set):take a set containing the colours .
    b_set(set):take a set containing the colours

    Returns:
    tupple:it returns   set containing all the colors from color_list_1 which
            are not present in color_list_2.
    '''

    return a_set-b_set
def main():
    
    a_set = set(input("Enter a colours with comma :").split(","))
    b_set = set(input("Enter a colours with comma :").split(","))
    print("The valus in the first set and not containing the second set:",check(a_set,b_set))
    



if __name__ == "__main__":
    main()