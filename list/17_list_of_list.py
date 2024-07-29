'''
    @Author: v sanjay kumar
    @Date: 2024-07-25 12:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 12:00:30.
    @Title : Python program to remove duplicates from a list of lists.

'''



def remove_duplicates(list_of_lists):
    '''
    Removes duplicate lists from a list of lists.

    Parameters:
    - list_of_lists (list): The list of lists.

    Returns:
    - list: A new list of lists with duplicates removed.
    '''
    seen = set()
    unique_list_of_lists = []

    for sublist in list_of_lists:
        tuple_sublist = tuple(sublist)  # Convert to tuple to make it hashable
        if tuple_sublist not in seen:
            unique_list_of_lists.append(sublist)
            seen.add(tuple_sublist)

    return unique_list_of_lists





def main():
    sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    new_list = remove_duplicates(sample_list)
    
    print("Original list:", sample_list)
    print("New list with duplicates removed:", new_list)






if __name__ == "__main__":
    main()
