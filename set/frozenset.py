'''
@Author: v sanjay kumar
@Date: 2024-07-24 03:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 03:00:30
@Title : Remove members in given set if element is present
'''


def remove_all(it_set):
    """
    descripton
      creat a frozen set .

    Parameters:
    - it_set (set): alredy given set.
    -element(int) : creat frozen set.
    Returns:
    - set-updated set.
    """
    return frozenset(it_set)
        



    
def main():
    it_set ={1,2,6,7,8,0,3,8,9}
    
    print("frozen set:",remove_all(it_set))



if __name__ =="__main__":
    main()