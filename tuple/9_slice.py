'''
    @Author: v sanjay kumar
    @Date: 2024-07-25 3:10:00
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 3:10:00
    @Title:program to slice a tuple.
'''

def remove_tuple(n_tup):
    """
    Description:
        Function to slice the tuple
    Parameters:
        tup (tuple): given tuple.
    Returns:
        tuple: after sliceing  .
    """
    new_tup = n_tup[0:4:1]

    return new_tup

def main():
    my_tup = (1, 2, 3, 4, 5)
    print("The new tuple is", remove_tuple(my_tup))

if __name__ == "__main__":
    main()
