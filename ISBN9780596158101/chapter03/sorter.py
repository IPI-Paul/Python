#!/usr/bin/env python3

# Example 3-6
# A Python program that sorts stdin text and can be applied to any data source 
# including output of other scripts.
# Author: Mark Lutz
# Last modified: 

import sys                              # or sorted(sys.stdin)
lines = sys.stdin.readlines()           # sort stdin input lines,
lines.sort()                            # send result to stdout
for line in lines:  print(line, end='') # for further processing

