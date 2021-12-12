# Listing 15.20
# Contains a recursive function named rev that accpets a list as a paremeter and
# returns a new list with all the elements of the original list in reverse order
# Author: Rick Halterman
# Last modified: 

def rev(lst):
    return [] if len(lst) == 0 else rev(lst[1:]) + lst[0:1]

print(rev([1, 2, 3, 4, 5, 6, 7]))