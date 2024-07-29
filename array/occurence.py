'''
   @Author: v sanjay kumar
   @Date: 2024-07-22 03:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-22 03:00:30
   @Title : occurence of elements
'''



def elementcount(arr):
    '''reverse all elements in the array.

    Parameters:
    func (function): takes the one array.

    Returns:
    reversed arr
    '''
    count_elements=()
    for i in arr:
        if i not in count_elements:
            print(f"the element{i},occure in {arr.count(i)}Times")

            count_elements.add(i)


def main():
    n =int(input('Enter a array length :'))
    arr =[]
    for _ in range(n):
        arr.append(int(input("Enter a number :")))
    print(arr)
    elementcount(arr)


if __name__ =="__main__":
    main()