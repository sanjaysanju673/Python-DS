'''
@Author: v sanjay kumar
@Date: 2024-07-24 05:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 05:30:30.
@Title : Python program to remove duplicates from a list
'''


def duplicate_list(sam_list):
    """
    descripton
       Remove The duplicates and print the resultent list.
'''

    Parameters:
    - it_list(list):  given list.

    Returns:
    - list1(list).-the final list which does not contains the duplicates
    
    """
    res =[]

    [res.append(x) for x in sam_list if x not in res] 
   
    return res
        



    
def main():
    sam_list =[1, 3, 5, 6, 3, 5, 6, 1]

    print("The original list is : " ,duplicate_list(sam_list))



if __name__ =="__main__":
    main()