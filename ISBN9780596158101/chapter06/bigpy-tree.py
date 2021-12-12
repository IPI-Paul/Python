#!/usr/bin/env python3

# Example 6-2
# Extends the first-cut solution that looks for the biggest Python file in a 
# directory and its subdirectories. It uses Python's pprint( 'pretty print') to 
# display the results
# Author: Mark Lutz
# Last modified: 

"""
Find the largest Python source file in an entire directory tree. Search the Python
source lib, use pprint to display results nicely
"""

import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
    # Windows
    dirname = r'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib'
else:
    dirname = '/usr/lib/python3.6'  # Unix, Linux, Cygwin


allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])