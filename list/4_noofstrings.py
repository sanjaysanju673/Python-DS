'''
@Author: v sanjay kumar
@Date: 2024-07-24 05:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 05:30:30.
@Title : Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings..
'''


def count_list(sam_list):
    """
    descripton
       Find count of the given conditions.
'''.

    Parameters:
    - it_list(list):  given list.

    Returns:
    - count(int).-count of the words the condition follows
    """
    count = 0
    for i in sam_list:
        l =list(i)
        if (len(i)>2 and l[0] == l[-1]):
           count += 1
        
    return count
        



    
def main():
    sam_list = ['abc', 'xyz', 'aba', '1221']

    
    
    print("the final count is",count_list(sam_list))


if __name__ =="__main__":
    main()