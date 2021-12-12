# Listing 15.6
# Implements a binary search algorithm as a Python function
# Author: Rick Halterman
# Last modified: 

def binary_search(lst, seek):
    """
    Returns the index of element seek in list lst, if seek is present in lst.
    Returns None if seek is not an element of lst.
    lst: is the list in which to search
    seek: is the element to find
    """
    first = 0           # Initialise the first position in list
    last = len(lst) - 1 #Initialise the last position in list
    while first <= last:
        # mid is middle position in the list
        mid = first + (last - first + 1) // 2   # Note: Integer division
        if lst[mid] == seek:
            return mid      # Found it
        elif lst[mid] > seek:
            last = mid - 1  # Continue with 1st half
        else:   # v[mid] < seek
            first = mid + 1 # continue with 2nd half
    return None     # Not there

def format(i):
    """
    Prints integer i right justified in a 4-space horizontal area. Prints '****'
    if i > 9,999
    """
    if i > 9999:
        print('****')       # Too big
    else:
        print('{0:>4}'.format(i))

def show(lst):
    """
    Prints the contents of list lst
    """
    for item in lst:
        # Print element right justifies in 4 spaces
        print('{0:>4}'.format(item), end='') 
    print()         # Print newline

def draw_arrow(value, n):
    """
    Print an arrow to value which is an element in a list.
    n: specifies the horizontal offest of the arrow
    """
    # + is the centre of '-- ' therefore 7 character spacing needed
    print(('{0:>' + str(n) + '}').format('   ^   '))
    print(('{0:>' + str(n) + '}').format('   |   '))
    print(('{0:>' + str(n) + '}{1}').format('   +-- ', value))

def display(lst, value):
    """
    Draws an ASCII art arrow showing where the given value is within the list.
    lst: is the list
    value: is the element to locate
    """
    show(lst)           # Print contents of the list
    position = binary_search(lst, value)
    if position != None:
        position = 4 * position + 7 # Compute spacing for arrow
        draw_arrow(value, position)
    else:
        print('(', value, ' not in list)', sep='')
    print()

def main():
    a = [2, 5, 11, 13, 44, 80, 100, 110]
    display(a, 13)
    display(a, 2)
    display(a, 7)
    display(a, 100)
    display(a, 110)

main()    