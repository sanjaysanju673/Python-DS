'''
@Author: v sanjay kumar
@Date: 2024-07-24 11:24:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 11:24:30
@Title : find the difference  of the given sets
'''


def difference_all(first_set,second_set):
    """
    descripton
      Takes the two sets and returns the differece of the two sets .

    Parameters:
    - first_set (set): First set user given.
    -esecond_set(set) : second set user given.
    Returns:
    - set-updated set.
    """
    set3 =first_set.difference(second_set)
    return set3
    


def main():
    first_set ={"sanjay",1,4,3,8,9,False,"True"}
    second_set=set((1,2,3,4,5,6,7,8,9))
    print("The difference set is:",difference_all(first_set,second_set))



if __name__ =="__main__":
    main()