#!/usr/bin/env python3

# Example 19-1
# Uses string splitting to sum columns of file data
# Author: Mark Lutz
# Last modified: 

def summer(numCols, fileName):
    sums = [0] * numCols                    # make list of zeros
    for line in open(fileName):             # scan file's lines
        cols = line.split()                 # split up columns
        for i in range(numCols):            # around blanks/tabs
            if not ('__import__' in cols[i] and 'system' in cols[i]):
                sums[i] += eval(cols[i])    # add numbers to sums
    return sums

if __name__ == '__main__':
    import sys
    if not ('__import__' in sys.argv[1] and 'system' in sys.argv[1]):
        print(summer(eval(sys.argv[1]), sys.argv[2]))   # '% summer.py cols file'