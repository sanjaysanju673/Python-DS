'''
@Author: v sanjay kumar
@Date: 2024-07-23 1:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 1:30:30
@Title: Print Dictionary in Table Format
'''

def print_dict_table(dictionary):
    '''
    Print the given dictionary in a table format.

    Parameters:
    dictionary (dict): The dictionary to print in table format.

    Returns:
    None
    '''
    # Determine the maximum width for each column
    key_width = max(len(str(key)) for key in dictionary.keys())
    value_width = max(len(str(value)) for value in dictionary.values())
    
    # Print the header
    print(f"{'Key'.ljust(key_width)} | {'Value'.ljust(value_width)}")
    print("-" * (key_width + value_width + 3))
    
    # Print each key-value pair
    for key, value in dictionary.items():
        print(f"{str(key).ljust(key_width)} | {str(value).ljust(value_width)}")

def main():
    my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
    print("Dictionary in table format:")
    print_dict_table(my_dict)

if __name__ == "__main__":
    main()
