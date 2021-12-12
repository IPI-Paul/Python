#!/usr/bin/env python3

# Example 6-14
# Codes a portable and general command-line tool, with support for arguments, 
# exception processing, tracing, and list-only mode.
# Author: Mark Lutz
# Last modified: 

"""
delete all.pyc bytecode files in a directory tree: use the command line args as 
root if given, else current working dir
"""

import os , sys
findonly = False
rootdir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]

found = removed = 0
for (thisDirLevel, subsHere, filesHere) in os.walk(rootdir):
    for filename in filesHere:
        if filename.endswith('.pyc'):
            fullname = os.path.join(thisDirLevel, filename)
            print('=>', fullname)
            if not findonly:
                try:
                    os.remove(fullname)
                    removed += 1
                except:
                    type, inst = sys.exc_info()[:2]
                    print('*' * 4, 'Failed', filename, type, inst)
            found += 1
print('Found', found, 'files, removed', removed)