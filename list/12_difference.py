'''
@Author: v sanjay kumar
@Date: 2024-07-25 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 11:30:30.
@Title :a Python program to get the difference between the two lists.

'''

def dif_list(sam_list,sam_list1):
    ''''
    descripton
       get the difference between the two lists.


    Parameters:
    - sam_list(list):  given list.
    - sam_list1(list): second list

    Returns:
    - diference(list).-return the difference of two list.
'''
    
    diference = [x for x in sam_list if x not in sam_list1]

    return diference

        
    
            



    
def main():
    sam_list =[1,3,4,5,6,7,8,9,10]
    sam_list1 = [1,67,89,6,4,3,2,2,1]
    
    print("the difference between of two lists: " ,dif_list(sam_list,sam_list1))



if __name__ =="__main__":
    main()