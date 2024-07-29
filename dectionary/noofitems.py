'''
@Author: v sanjay kumar
@Date: 2024-07-23 03:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 03:30:30
@Title: Count Number of Items in Dictionary Values that are Lists
'''

def count_list_items(dictionary):
    '''
    Count the number of items in dictionary values that are lists.

    Parameters:
    dictionary (dict): The dictionary with values that may be lists.

    Returns:
    int: The total count of items in all list values.
    '''
    total_count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            total_count += len(value)
    return total_count

def main():
    sample_dict = {
        'fruits': ['apple', 'banana', 'cherry'],
        'numbers': [1, 2, 3, 4],
        'colors': ['red', 'green'],
        'single_value': 'hello',
        'empty_list': []
    }
    
    result = count_list_items(sample_dict)
    print(f"Total number of items in list values: {result}")

if __name__ == "__main__":
    main()
