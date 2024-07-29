'''
@Author: v sanjay kumar
@Date: 2024-07-25 12:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 12:30:30.
@Title : Python program to check whether two lists are circularly identical.
'''

def are_circularly_identical(list1, list2):
    '''
    Checks whether two lists are circularly identical.

    Parameters:
    - list1 (list): The first list.
    - list2 (list): The second list.

    Returns:
    - bool: True if the lists are circularly identical, False otherwise.
    '''
    if len(list1) != len(list2):
        return False

    combined_list = list1 + list1
    return any(combined_list[i:i+len(list2)] == list2 for i in range(len(list1)))

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 1, 2]
    
    if are_circularly_identical(list1, list2):
        print("The two lists are circularly identical.")
    else:
        print("The two lists are not circularly identical.")

if __name__ == "__main__":
    main()
