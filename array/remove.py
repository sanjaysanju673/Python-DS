'''
   @Author: v sanjay kumar
   @Date: 2024-07-22 03:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-22 03:00:30
   @Title : occurence of elements
'''



def elementcount(arr,ele):
    '''reverse all elements in the array.

    Parameters:
    func (function): takes the one array.

    Returns:
    reversed arr
    '''
    
    for i in arr:
        if (i == ele):
            arr.remove(ele)
    return arr


def main():
    n =int(input('Enter a array length :'))
    arr =[]
    for _ in range(n):
        arr.append(int(input("Enter a number :")))
    print(arr)
    ele = int(input("Enter a want remove element"))
    print("after remove the element the arr is :",elementcount(arr,ele))


if __name__ =="__main__":
    main()