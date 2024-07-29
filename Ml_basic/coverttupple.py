'''
@Author: v sanjay kumar
@Date: 2024-07-22 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 11:30:30
@Title :check the the element contens or not
'''

def check(a_list):
    '''the function takes the   list and   and returns  the tupple.

    Parameters:
    anonamas_list(list):  list .

    Returns:
    tupple:it returns converted tupple
    '''

    return str(a_list)
def main():
    
    a_list =list(map(int,input('Enter a list Values: ')))


    print("The converted string is :",check(a_list))
    print(type(check(a_list)))



if __name__ == "__main__":
    main()