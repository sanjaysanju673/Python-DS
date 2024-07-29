'''
@Author: v sanjay kumar
@Date: 2024-07-23 03:14:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 03:14:30
@Title: Check Multiple Keys Exist in a Dictionary
'''

def check_keys_exist(dictionary, keys):
    '''
    Check if multiple keys exist in a dictionary.

    Parameters:
    dictionary (dict): The dictionary to check.
    keys (list): The list of keys to check for existence in the dictionary.

    Returns:
    bool: True if all keys exist, False otherwise.
    '''
    return all(key in dictionary for key in keys)

def main():
    sample_dict = {'id': 1, 'success': True, 'name': 'Lary', 'age': 25,'raju':24,'ram':26}
    keys_to_check = ['id', 'name', 'age']
    
    result = check_keys_exist(sample_dict, keys_to_check)
    print(f"All keys {keys_to_check} exist in the dictionary: {result}")

if __name__ == "__main__":
    main()
