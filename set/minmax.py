'''
@Author: v sanjay kumar
@Date: 2024-07-24 03:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 03:00:30
@Title : Find the maximam and minimum Elements in the given set.
'''


def maxmin(it_set):
    """
    descripton
       Find the maximam and minimum Elements in the given set.

    Parameters:
    - it_set (set): alredy given set.

    Returns:
    - maximum element(int).
    - minimum elements(int).
    """
    return max(it_set),min(it_set)
        



    
def main():
    it_set ={1,2,6,7,8,0,3,8,9}
    
    maximum, minimum =maxmin(it_set)
    print("The maximum and minimum Elements are",maximum,minimum)


if __name__ =="__main__":
    main()