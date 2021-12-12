#!/usr/bin/env python3

# Example 6-1
# Is a first-cut solution that looks for the biggest Python file in one directory
# Author: Mark Lutz
# Last modified: 

"""
Find the largest Python source file in a single directory. Search Windows Python
source lib, unless dir command-line arg
"""

import os, glob, sys
dirname = r'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib' \
          if len(sys.argv) == 1 else sys.argv[1]
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])