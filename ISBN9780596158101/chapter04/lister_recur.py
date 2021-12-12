#!/usr/bin/env python3

# Example 4-5
# This function is almost the same as lister in Example 4-4 but calls os.listdir
# to generate file paths manually and calls itself recursively todescend into 
# subdirectories
# Author: Mark Lutz
# Last modified: 

'list files in dir tree by recursion'

import sys, os

def mylister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):                # list files here
        path = os.path.join(currdir, file)          # add dir path back
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path)                          # recur into subdirs

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mylister(sys.argv[1])                       # dir name in cmdline