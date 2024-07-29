'''
@Author: v sanjay kumar
@Date: 2024-07-25 10:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 10:30:30.
@Title :Python function that takes two lists and returns True if they have at
         least one common member.

'''

def comman_list(sam_list,sam_list1):
    ''''
    descripton
       print the true if the given lists having at least one comman member.


    Parameters:
    - sam_list(list):  given list.

    Returns:
    - (boolean).-if the given lists having a one comman member.
'''
    for i in sam_list1:
        for j in sam_list1:
            if i == j: 
                return True
            else:
                return False

        
    
            



    
def main():
    sam_list =[1,3,4,5,6,7,8,9,10]
    sam_list1 = [1,67,89,6,4,3,2,2,1]
    
    print("the comman member in the given two lists is: " ,comman_list(sam_list,sam_list1))



if __name__ =="__main__":
    main()