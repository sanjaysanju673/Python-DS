'''
@Author: v sanjay kumar
@Date: 2024-07-23 1:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 1:30:30
@Title :convert string to dectionary
'''

def strtodict(given_str):
    '''
    convert string to dictionory.
    Parameters:
    dictionary (dict): The dictionary to sort.
    Return:
    converted dictonary
    '''
    keys =[]
    values =[]
    count1 =set()
    for i in list(given_str):
        if i not in count1:
            values.append(given_str.count(i))
            keys.append(i)
            count1.add(i)
    print(values)
    dictionary = dict(zip(keys,values))
    return dictionary


def main():
    given_str =input("Enter a string :")
    print("New dictionary",strtodict(given_str))


if __name__ == "__main__":
    main()