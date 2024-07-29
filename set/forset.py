'''
@Author: v sanjay kumar
@Date: 2024-07-18 05:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 05:00:30
@Title : Check Whether a File Exists
'''


def set_all(it_set):
    """
    descripton
      prints the all elements up to the end of the list.

    Parameters:
    - n (int): The number in the set.

    Returns:
    - none
    """

    for i in range(len(it_set)):
        print("The element in the set is",it_set[i])

    
def main():
    it_set =(1,2,3,4,5,6,7,8,9)
    
    set_all(it_set)

if __name__ =="__main__":
    main()