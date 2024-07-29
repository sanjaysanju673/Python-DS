'''
@Author: v sanjay kumar
@Date: 2024-07-23 12:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 12:00:30
@Title :iterate all elements in  dectionary
'''



def all_dict(dictionary):
    '''
    Add the element to dictionary.

    Parameters:
    dictionary (dict): The dictionary .

    Returns:
    None
    '''
    for item in dictionary.items():
        print(f"the element of dictionary is{item}:")
    
    for key in dictionary.keys():
        print("the dictionary key are",key)
    
    for value in dictionary.values():
        print("the value of the dictionory is",value)

def main():
    keys = list(map(int, input("Enter the dictionary keys separated by spaces: ").split()))
    values = list(map(str, input("Enter the dictionary values separated by commas: ").split(","))) 
    if len(keys) != len(values):
        print("The number of keys and values do not match!")
        return
    
    dictionary = dict(zip(keys, values))
    print("the dictionory:",dictionary)
    all_dict(dictionary)


if __name__ == "__main__":
    main()


