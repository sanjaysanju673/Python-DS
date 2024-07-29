'''
@Author: v sanjay kumar
@Date: 2024-07-25 12:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 12:00:30.
@Title : Python program to append a list to the second list.

'''

def dif_list(f_list,se_list1):
    ''''
    descripton
       get the difference between the two lists.


    Parameters:
    - sam_list(list):  given list.
    - sam_list1(list): second list

    Returns:
    - diference(list).-return the difference of two list.
'''
    final_list = f_list + se_list1
    
    return final_list

        
    
            



    
def main():
    first_list =[1,3,4,5,6,7,8,9,10]
    second_list1 = [1,67,89,6,4,3,2,2,1]
    
    print("the final results are after appending first and second list: " ,dif_list(first_list,second_list1))



if __name__ =="__main__":
    main()