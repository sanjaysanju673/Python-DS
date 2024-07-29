'''
@Author: v sanjay kumar
@Date: 2024-07-24 03:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 04:00:30
@Title : Python program to sum all the items in a list..
'''


def sum_list(it_list):
    """
    descripton
       Find the sum  of the Elements in the given list.

    Parameters:
    - it_list(list): alredy given set.

    Returns:
    - sum(int).-all elements sum
    
    """
    sum = 0
    for i in it_list:
        sum = sum+i
        
    return sum
        



    
def main():
    it_list =[1,2,6,7,8,0,3,8,9]
    
    
    print("The sum of  Elements in list  is",sum_list(it_list))


if __name__ =="__main__":
    main()