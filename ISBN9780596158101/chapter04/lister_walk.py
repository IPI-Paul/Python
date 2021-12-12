#!/usr/bin/env python3

# Example 4-4
# Uses a for loop and os.walk to retrieve files and subdirectories from a path
# Author: Mark Lutz
# Last modified: 

'list file tree with os.walk'

import sys, os

def lister(root):                                       # for a root dir
    # generate dirs in tree
    for (thisdir, subshere, fileshere) in os.walk(root):
        print('[' + thisdir +']')
        for fname in fileshere:                         # print files in this dir
            path = os.path.join(thisdir, fname)         # add dir name prefix
            print(path)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        lister(sys.argv[1])                             # dir name in cmdline