'''
@Author: v sanjay kumar
@Date: 2024-07-23 11:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-23 11:00:30
@Title :sort dectionary
'''



def add_dict(dict1,dict2,dict3):
    '''
    concatinate the two dictionorys.

    Parameters:
    dictionary (dict): The dictionary to sort.

    Returns:
    None
    '''
    for i in dict2.keys():
        dict1[i] =dict2[i]
    
    for j in dict3.keys():
        dict[j] = dict3[j]

    
    print("After adding   dictionarys  result is:", dict1)

def main():
    dict1={1:10,2:20}
    dict2 ={3:30,4:40}
    dict3 ={5:50,6:60}
    print("Before concadinations   the dictionorys is:",dict1,dict2,dict3)
    add_dict(dict1,dict2,dict3)


if __name__ == "__main__":
    main()