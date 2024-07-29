'''
    @Author: v sanjay kumar
    @Date: 2024-07-25 3:00:00
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 3:00:00
    @Title: Program to find the repeated items of a tuple.
'''

def find_repeated_items(n_tuple):
    """
    Description:
        Function to find the repeated items of a tuple.

    Parameters:
        tuple (tuple): Input tuple to check for repeated items.

    Returns:
        set: Set containing the repeated items.
    """
    seen = set()
    repeated = set()
    for item in n_tuple:
        if item in seen:
            repeated.add(item)
        else:
            seen.add(item)
    return repeated

def main():
    tup = (1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 2,8)
    print("The repeated items in the tuple are", find_repeated_items(tup))

if __name__ == "__main__":
    main()
