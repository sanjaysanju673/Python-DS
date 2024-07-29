'''
@Author: v sanjay kumar
@Date: 2024-07-23 3:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 3:00:30
@Title: Count Values Associated with Key in Dictionary List
'''

def count_key_value(dict_list, key, value):
    '''
    Count the number of dictionaries in the list that have a specific key with a specific value.

    Parameters:
    dict_list (list): The list of dictionaries to search.
    key (str): The key to look for in each dictionary.
    value (any): The value associated with the key to count.

    Returns:
    int: The count of dictionaries with the specified key-value pair.
    '''
    count = 0
    for dictionary in dict_list:
        if dictionary.get(key) == value:
            count += 1
    return count

def main():
    sample_data = [
        {'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}
    ]
    key_to_check = 'success'
    value_to_check = True
    
    result = count_key_value(sample_data, key_to_check, value_to_check)
    print(f"Count of dictionaries with '{key_to_check}' as {value_to_check}: {result}")

if __name__ == "__main__":
    main()
