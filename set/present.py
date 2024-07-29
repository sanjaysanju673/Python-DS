'''
@Author: v sanjay kumar
@Date: 2024-07-24 11:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 11:00:30
@Title : Remove members in given set if element is present
'''


def remove_all(it_set,element):
    """
    descripton
      Remove the elements in given set.

    Parameters:
    - it_set (set): alredy given set.
    -element(int) : user want to delete element.
    Returns:
    - set-updated set.
    """
    if (element in it_set):
        it_set.discard(element)
    else:
        print("The Element is not found!")
    return it_set
    
    
def main():
    it_set ={"sanjay",1,True,3,8,9}
    element =input("Enter a element if you want delete.")
    print("final list",remove_all(it_set,element))

if __name__ =="__main__":
    main()