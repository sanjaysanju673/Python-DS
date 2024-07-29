'''
    @Author: v sanjay kumar
    @Date: 2024-07-25 3:00:00
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 3:00:00
    @Title: Program to find the item is exist or not in a tuple.
'''

def find_exicited_items(n_tuple,ele):
    """
    Description:
        Function to find the a element exicited or not

    Parameters:
        tuple (tuple): Input tuple to check for repeated items.

    Returns:
        bool: returns the true the item is exicited otherwise false.
    """
    
    for item in n_tuple:
        if item == ele :
            return True
        
    return False

def main():
    tup = (1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 2,8)
    ele=int(input("Enter a check the element it is exicited or not:"))
    print("The element exicited in the tuple :", find_exicited_items(tup,ele))

if __name__ == "__main__":
    main()
