'''
@Author: v sanjay kumar
@Date: 2024-07-24 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 10:00:30
@Title : Add members to set
'''


def remove_all(it_set):
    """
    descripton
      Remove the elements in given list.

    Parameters:
    - it_set (set): alredy given set.

    Returns:
    - set-updated set.
    """
    it_set.discard("sanjay")
    it_set.discard("True")
    return it_set
    
    
def main():
    it_set ={"sanjay",1,True,3,8,9}
    print("final list",remove_all(it_set))

if __name__ =="__main__":
    main()