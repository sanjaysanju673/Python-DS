'''
@Author: v sanjay kumar
@Date: 2024-07-24 11:13:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-24 11:13:30
@Title : find the intersection of the given list
'''



def intersection_all(first_set,second_set):
    """
    descripton
      Takes the two sets and returns the intersection of the two sets .

    Parameters:
    - first_set (set): First set user given.
    -esecond_set(set) : second set user given.
    Returns:
    - set-updated set.
    """
    set3 =first_set.Symetric_difference(second_set)
    return set3



def main():
    first_set ={1,2,3,4}
    second_set={4,5,7,2}
    print("The intersection set is:",intersection_all(first_set,second_set))



if __name__ =="__main__":
    main()