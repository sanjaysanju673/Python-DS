'''
@Author: v sanjay kumar
@Date: 2024-07-22 11:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 11:00:30
@Title :check the the element contens or not
'''

def check(a_list,value):
    '''the function takes the  c list and  value and print the the value contains or not.

    Parameters:
    anonamas_list(list):  list .
    value = value(int)
   

    Returns:
    boolean:it returns true or false values
    '''

    return value in a_list

def main():
    
    a_list =list(map(int,input('Enter a list Values: ')))

    value = int(input("Enter a value:"))

    print("The given value in the list",check(a_list,value))




if __name__ == "__main__":
    main()