#!/usr/bin/env python3

# Example 18-23
# Is a first attempt at two simple reversal functions
# Author: Mark Lutz
# Last modified: 

def reverse(list):                  # recursive
    if list == []:
        return []
    else:
        return reverse(list[1:]) + list[:1]

def ireverse(list):                 # iterative
    res = []
    for x in list: res = [x] + res
    return res