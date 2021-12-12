#!/usr/bin/env python3

# Example 3-7
# A Python program that sums stdin text and can be applied to any data source 
# including output of other scripts.
# Author: Mark Lutz
# Last modified: 

import sys
sum = 0 
while True:
    try:
        line = input()                      # or call sys.stdin.readlines()
    except EOFError:                        # or for line in sys.stdin:
        break                               # input strips \n at end
    else:
        sum += int(line)                    # was sting.atoi() in 2nd ed
print(sum)