'''
@Author: v sanjay kumar
@Date: 2024-07-18 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 10:00:30
@Title :create list and tuple
'''

def convertlist(userinput):
    '''
    the function takes the  accepts a sequence of comma-separated numbers from user
    and generate a list and a tuple with those numbers.

    Parameters:
    numbers(str): take the numbers .
   

    Returns:
    list:it return the list and tuple
    '''
    user_list = list(userinput.split(","))
    user_tuple = tuple(userinput.split(","))
    return user_list,user_tuple



def main():
    userinput = input("Enter only number with commas: ")
    user_list,user_tuple = convertlist(userinput)
    print('the converted list and tupple is',user_list,user_tuple)


if __name__ == "__main__":
    main()
