'''

    @Author: v sanjay kumar
    @Date: 2024-07-25 2:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-25 2:00:30
    @Title :create tuple with different data types.

'''


def creattuple():
    """
    Description:
        create tuple with difference data type.

    Parameters:
        void (none): none.

    Returns:
        set: return the new tuple .
    """
    x =list((1,2,3,4,5,6,9))
  
    return tuple(x)


def main():
    x=creattuple()
    y ="sanjay kumar shyam"
    z =tuple(y)
    print(z)
    print(x)
   


if __name__ == "__main__":
    main()