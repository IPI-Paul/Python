#!/usr/bin/env python3

# Example 18-24
# Fixes both problems of the rev1 by using generic sequence and returns the 
# empty sequence itself, rather than an empty list constant
# Author: Mark Lutz
# Last modified: 

def reverse(list):
    if not list:                            # empty? (not always [])
        return list                         # the same sequence type
    else:
        return reverse(list[1:]) + list[:1] # add front item on the end

def ireverse(list):
    res = list[:0]                          # empty, of some type
    for i in range(len(list)):
        res = list[i:i+1] + res             # add each item to front
    return res