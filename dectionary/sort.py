'''
@Author: v sanjay kumar
@Date: 2024-07-23 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 10:00:30
@Title :sort dectionary
'''



def sort_dict(dictionary):
    '''
    Sort the given dictionary in ascending and descending order.

    Parameters:
    dictionary (dict): The dictionary to sort.

    Returns:
    None
    '''
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    
    rev_sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    
    print("After sorting the dictionary in ascending order:", sorted_dict)
    print("After sorting the dictionary in descending order:", rev_sorted_dict)


def main():
    keys = list(map(int, input("Enter the dictionary keys separated by spaces: ").split()))
    values = list(map(str, input("Enter the dictionary values separated by commas: ").split(",")))
    
    if len(keys) != len(values):
        print("The number of keys and values do not match!")
        return
    
    dictionary = dict(zip(keys, values))
    
    sort_dict(dictionary)


if __name__ == "__main__":
    main()



if __name__ =="__main__":
    main()