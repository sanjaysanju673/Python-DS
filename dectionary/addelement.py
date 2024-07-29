'''
@Author: v sanjay kumar
@Date: 2024-07-23 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 10:00:30
@Title :add element to  dectionary
'''



def sort_dict(dictionary):
    '''
    Add the element to dictionary.

    Parameters:
    dictionary (dict): The dictionary to sort.

    Returns:
    None
    '''
    dictionary[4]='ram'
    dictionary[5]= 'rajesh'
    dictionary.update({6:"ravi",7:"radha"})
    print("After adding element in  the dictionary r:", dictionary)


def main():
    keys = list(map(int, input("Enter the dictionary keys separated by spaces: ").split()))
    values = list(map(str, input("Enter the dictionary values separated by commas: ").split(","))) 
    if len(keys) != len(values):
        print("The number of keys and values do not match!")
        return
    
    dictionary = dict(zip(keys, values))
    print("Before adding element in the dictionory:",dictionary)
    sort_dict(dictionary)


if __name__ == "__main__":
    main()


