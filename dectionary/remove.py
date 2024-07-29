'''
@Author: v sanjay kumar
@Date: 2024-07-23 1:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 1:00:30
@Title :remove the element in the dectionary
'''



def remove_dict(dict1,key):
    '''
    remove the element in the dictionory.

    Parameters:
    dictionary (dict): The dictionary to sort.

    Returns:
    removed value
    '''
    if key in dict1:
        removed_value=dict1.pop(key)
        print("After remove the specifed key then the dectionary is:",dict1)
        return removed_value
    else:
        print("key error! The key is not found ")
    
    


def main():
    dict1={1:10,2:20,3:30,4:40,5:50,6:60}
    key = int(input("enter a key :"))
    print("Before remove the element the dictionorys is:",dict1)
    print("Removed value is",remove_dict(dict1,key))


if __name__ == "__main__":
    main()