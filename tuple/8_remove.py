'''
    @Author: v sanjay kumar
    @Date: 2024-07-25 3:10:00
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 3:10:00
    @Title: Program to remove the element in the tuple.
'''

def remove_tuple(n_tup):
    """
    Description:
        Function to remove the element in the tuple
    Parameters:
        tup (tuple): given tuple.
    Returns:
        tuple: after removeing .
    """
    list1 =list(n_tup)
    print(list1.pop())
    return tuple(list1)

def main():
    my_tup = (1, 2, 3, 4, 5)
    print("the before removie",my_tup)
    print("The new tuple is", remove_tuple(my_tup))
    print(type(remove_tuple(my_tup)))

if __name__ == "__main__":
    main()
