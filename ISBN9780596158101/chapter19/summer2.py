#!/usr/bin/env python3

# Example 
# Uses string splitting to sum columns of file data
# Author: Mark Lutz
# Last modified: 

def summer(numCols, fileName):
    sums = [0] * numCols                    
    for line in open(fileName):             # use file iterators
        cols = line.split(',')              # assume comma-delimited
        nums = [int(x) for x in cols]       # use limited converter
        both = zip(sums, nums)              # avoid nested for loop
        sums = [x + y for (x, y) in both]
    return sums

if __name__ == '__main__':
    import sys
    if not ('__import__' in sys.argv[1] and 'system' in sys.argv[1]):
        print(summer(eval(sys.argv[1]), sys.argv[2]))   # '% summer.py cols file'