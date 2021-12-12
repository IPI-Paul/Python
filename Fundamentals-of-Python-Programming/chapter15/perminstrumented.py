# Listing 15.14
# Instruments the perm function by adding print statements that indicate the 
# state of its list as it loops and calls itself recursively
# Author: Rick Halterman
# Last modified: 

def perm(lst, begin, result, depth):
    """
    Creates a list (result) containing all the permutations of the elements of a
    given list (lst_), beginning with a specified index (begin). 
    Printing statements report the progression of the function's recursion. The 
    depth parameter indicates the depth of the recursion. 
    This is a helper function for the permutations function
    """
    print('  ' * depth, 'begin =', begin)
    end = len(lst) - 1  # Index of the last element
    if begin == end:
        result += [lst[:]]      # Copy lst into result
        print('  ' * depth, ' *')
    else:
        for i in range(begin, end + 1):     # Consider all indices
            # Interchange the element at the first position with the element at 
            # position i
            lst[begin], lst[i] = lst[i], lst[begin]
            print('  ' * depth, '  ', lst[begin], '<-->', lst[i], ' ', lst)
            # Recursively permute the rest of the list
            perm(lst, begin + 1, result, depth + 1)
            # Undo the earlier interchange
            lst[begin], lst[i] = lst[i], lst[begin]

def permutations(lst):
    """
    Returns a list containing all the permutations of the orderings of the 
    elements of a given list (lst). Delegates the hard work to the perm function
    """
    result = []
    perm(lst, 0, result, 0) # Intial call with depth = 0
    return result

def main():
    """
    Tests the permutations function
    """
    a = list(range(3))      # Make list [0, 1, 2]
    print(permutations(a))

if __name__ == '__main__':
    main()