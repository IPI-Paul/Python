#!/usr/bin/env python3

# Example 18-9
# Uses Python's variable-length argument lists feature to compute the intersection
# and union of arbitrarily many operands
# Author: Mark Lutz
# Last modified: 

"set operations for multiple sequences"

def intersect(*args):
    res = []
    for x in args[0]:                       # scan the first list
        for other in args[1:]:              # for all other arguments
            if x not in other: break        # this item in each one?
        else:
            res.append(x)                   # add common itmes to the end
    return res

def union(*args):
    res = []
    for seq in args:                        # for all sequence-arguments
        for x in seq:                       # for all nodes in argument
            if not x in res:
                res.append(x)               # add new items to result
    return res