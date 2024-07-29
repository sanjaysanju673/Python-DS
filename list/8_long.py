'''
@Author: v sanjay kumar
@Date: 2024-07-25 10:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-25 10:30:30.
@Title :Python n program to find the list of words that are longer than n from a
           given list of words.
'''


def longword_list(sam_list):
    """
    descripton
       find the longest lenth of the word in the given words in the list.
'''

    Parameters:
    - sam_list(list):  given list.

    Returns:
    - long(str).-longest word in  the given list.
    
    """
    long =sam_list[0]
    for i in sam_list:
        if (len(i)>len(long)):
            long =i
            

    return long 

    
    
            



    
def main():
    sam_list =['sanjay', 'sam', 'santhosh','sahas','sahasra', 'suhas', 'suhasini', 'shyam']
    
    print("The long word in the given list: " ,longword_list(sam_list))



if __name__ =="__main__":
    main()