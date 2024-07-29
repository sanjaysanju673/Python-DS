'''
@Author: v sanjay kumar
@Date: 2024-07-22 02:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 02:00:30
@Title : create array
'''



def arrayaccess(arr):
    '''Prints all elements in the array.

    Parameters:
    func (function): takes the one array.

    Returns:
    None
    '''
    for i in range(len(arr)):
        print("The element in the array",arr[i])




def main():
    n =int(input('Enter a array length :'))
    arr =[]
    for _ in range(n):
        arr.append(int(input("Enter a number :")))
    
    arrayaccess(arr)




if __name__ =="__main__":
    main()