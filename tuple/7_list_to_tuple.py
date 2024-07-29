'''
    @Author: v sanjay kumar
    @Date: 2024-07-25 3:30:00
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 3:30:00
    @Title: Program to convert a list to a tuple.
'''

def convert_list_to_tuple(n_list):
    """
    Description:
        Function to convert a list to a tuple.

    Parameters:
        list (list): Input list to be converted.

    Returns:
        tuple: Converted tuple from the input list.
    """
    return tuple(n_list)

def main():
    my_list = [1, 2, 3, 4, 5]
    print("The converted tuple is", convert_list_to_tuple(my_list))

if __name__ == "__main__":
    main()
