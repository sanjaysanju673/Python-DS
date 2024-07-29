'''
@Author: v sanjay kumar
@Date: 2024-07-24 04:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 04:00:30
@Title : Python program to multiplies all the items in a list..
'''


def mut_list(it_list):
    """
    descripton
       Find the multiplies all the Elements in the given list.

    Parameters:
    - it_list(list):  given list.

    Returns:
    - mut(int).-all elements mutliplies
    
    """
    mut = 1
    for i in it_list:
        mut = mut*i
        
    return mut
        



    
def main():
    it_list =[1,2,6,7,8,3,8,9]
    
    
    print("The multiplication of  all Elements in list  is",mut_list(it_list))


if __name__ =="__main__":
    main()