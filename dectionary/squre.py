'''
@Author: v sanjay kumar
@Date: 2024-07-23 12:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 12:30:30
@Title :find the squre of the given valus in dectionary.
'''



def squre_dict(keys,valus):
    '''
    Add keys and values to dictionary.

    Parameters:
    keys(int): keys .
    values(int):values
    Returns:
    Dectionory
    '''
    dictionary = dict(zip(keys, valus))
    return dictionary
    
def main():
    n =int(input("Enter a range you want: "))
    keys =[i for i in range(1,n)]
    values =[i*i for i in range(1,n)]
    if len(keys) != len(values):
        print("The number of keys and values do not match!")
        return
    
    
    print("The dictionory:",squre_dict(keys,values))
    


if __name__ == "__main__":
    main()


