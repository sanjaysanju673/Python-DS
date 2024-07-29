'''
@Author: v sanjay kumar
@Date: 2024-07-24 11:24:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 11:24:30
@Title : program to count the number of characters (character frequency) in a string.

'''


def Occurence_all(given_string):
    """
    descripton
      function to count the number of characters (character frequency) in a string .

    Parameters:
    - given_string (set):string is  user given.

    Returns:
    - dict -the dictionory contains the character and count.
    """
    repeated = set()
    keys = []
    count = []
    for i in given_string:
        if i  not in  repeated:
           count.append(ord(i))
           repeated.add(i)
           keys.append(i)
        else:
            continue
    return dict(zip(keys,count))       
             
            
   
    
def main():
    string = input("Enter a string : ")
    
    print("The occurence of the each character:",Occurence_all(string))

if __name__ =="__main__":
    main()