'''
@Author: v sanjay kumar
@Date: 2024-07-18 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 10:00:30
@Title :first and last colours print
'''

def colours(colour_list):
    '''the function takes the  colours list and print last and first colour.

    Parameters:
    colour_list(list): colour list .
   

    Returns:
    str,str:it returns the first and last colours
    '''

    return colour_list[0],colour_list[-1]

def main():
    try:
        colour= input("Enter a colous with comma sapareted :").split(",")
        
    except ValueError:
        print("Enter only characters")
    colour_list =list(colour)
    first_colour, last_colour =colours(colour_list)

    print("the first and last colours are",first_colour,last_colour)



if __name__ == "__main__":
    main()