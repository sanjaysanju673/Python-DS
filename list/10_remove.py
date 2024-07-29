'''
@Author: v sanjay kumar
@Date: 2024-07-25 10:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 10:30:30.
@Title :Python program  remove the 0th,4th,5th values in list

'''

def comman_list(sam_list):
    ''''
    descripton
       Return the final list after removing the 0th,4th and 5th elements in list.


    Parameters:
    - sam_list(list):  given list.

    Returns:
    - list.-final list after remove the 0th,4th,5th elements in list.
'''
    sam_list.remove(sam_list[0])
    sam_list.remove(sam_list[4])
    sam_list.remove(sam_list[3])

    return sam_list


        
    
            



    
def main():
    remove_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    
    print("The final list: " ,comman_list(remove_List))



if __name__ =="__main__":
    main()