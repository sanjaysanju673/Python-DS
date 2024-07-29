'''
@Author: v sanjay kumar
@Date: 2024-07-25 12:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 12:30:30.
@Title : Python program to check whether two lists are have the common elements are not.
'''

def are_having_common(list1, list2):
    '''
    Checks whether two lists are having common elements are not.

    Parameters:
    - list1 (list): The first list.
    - list2 (list): The second list.

    Returns:
    - common elements(list): Return the common elements in the both list.
    '''
    list3 =[]
    for i in range(len(list1)):
        for j in range(i+1,len(list2)):
            if list1[i] == list2[j]:
                list3.append(list1[i])

    return list3 



def main():
    list1 =[1,4,5,6,7,8,9,90,7,6,5,4,2]
    list2 =[]
    if are_having_common(list1, list2):
        print("The two lists are have the common elements.",are_having_common(list1,list2))
    else:
        print("The two lists are not having the common elements.")

if __name__ == "__main__":
    main()
