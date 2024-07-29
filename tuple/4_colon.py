'''

    @Author: v sanjay kumar
    @Date: 2024-07-25 2:30:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 2:30:30
    @Title : program to create the colon of a tuple..

'''


def clone_tuple(n_tuple):
    """
    Description:
        function to create the colon of a tuple.

    Parameters:
        tuple (tuple): take the tuple.

    Returns:
      sum(tuple): Returned the colon of the tuple in new tuple .
    """
    new_tuple =n_tuple[2:5]
    return new_tuple
  

def main():
   tup =(1,2,4,5,4,5)

   print("the new clone tuple is",clone_tuple(tup))


if __name__ == "__main__":
    main()