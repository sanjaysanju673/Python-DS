'''

    @Author: v sanjay kumar
    @Date: 2024-07-25 2:30:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 2:30:30
    @Title :program to unpack a tuple in several variables.

'''


def sum_tuple(n_tuple):
    """
    Description:
        program to unpack a tuple in several variables.

    Parameters:
        tuple (tuple): take the tuple.

    Returns:
      sum(int): caluculate the sum of all unpacked numbers .
    """
    n1,n2,n3,n4 =n_tuple
    
    return n1+n2+n3+n4


def main():
   tup =(1,2,4,5)
   for x in tup:
       print(x)
   print("the sum of unpacked elements in given tuple",sum_tuple(tup))


if __name__ == "__main__":
    main()