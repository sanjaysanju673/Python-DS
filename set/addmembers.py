'''
@Author: v sanjay kumar
@Date: 2024-07-18 05:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 05:00:30
@Title : Add members to set
'''


def add_all(it_set):
    """
    descripton
      prints the all elements up to the end of the list.

    Parameters:
    - it_set (set): alredy given set.

    Returns:
    - none
    """
    n =int(input("Enter a how many elements you want to add: "))
    for i in range(n):
        it_set.add(int(input("Enter element do you want to add :")))
    return it_set
    
def main():
    it_set =set()
    print("final list",add_all(it_set))

if __name__ =="__main__":
    main()