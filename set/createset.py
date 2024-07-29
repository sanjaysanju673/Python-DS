'''

    @Author: v sanjay kumar
    @Date: 2024-07-18 12:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-18 3:00:30
    @Title :create set

'''


def creatset():
    """
    Description:
        create set.

    Parameters:
        void (none): none.

    Returns:
        set: return the set.
    """
    x =set()
    x.add(2)
    x.add(7)
    return x


def main():
    x=creatset()
    print(x)
    


if __name__ == "__main__":
    main()