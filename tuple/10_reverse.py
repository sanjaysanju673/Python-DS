'''
    @Author: v sanjay kumar
    @Date: 2024-07-25 3:10:00
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 3:10:00
    @Title:program to reverse a tuple.
'''

def reverse_tuple(n_tup):
    """
    Description:
        Function to reverse the tuple
    Parameters:
        tup (tuple): given tuple.
    Returns:
        tuple: after reversening tuple .
    """
    
    return n_tup[::-1]

def main():
    my_tup = (1, 2, 3, 4, 5)
    print("The new tuple is", reverse_tuple(my_tup))

if __name__ == "__main__":
    main()
