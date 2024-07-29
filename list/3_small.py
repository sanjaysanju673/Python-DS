'''
@Author: v sanjay kumar
@Date: 2024-07-24 04:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 04:30:30.
@Title : Python program to get the smallest number from a list.
'''


def small_list(it_list):
    """
    descripton
       Find  the smallest number from a list.
'''.

    Parameters:
    - it_list(list):  given list.

    Returns:
    - small(int).-smallest number in the list
    
    """
    small = it_list[0]
    for i in it_list:
       if small >i:
           small = i
        
    return small
        



    
def main():
    it_list =[1,2,6,7,8,3,8,9]
    
    
    print("The smallest number of  all Elements in list  is",small_list(it_list))


if __name__ =="__main__":
    main()