#!/usr/bin/env python3

# Example 6-6
# Puts the parts created by split.py back together
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
join all part files in a dir created by split.py, to recreate file. This is 
roughly like a 'cat fromdir/* > tofile' command on unix, but is more portable 
and configurable, and exports the join operation as a reusable function. Relies
on sort order filenames: must be same length. Could extend split/join to pop up 
Tkinter file selectors
################################################################################
"""

import os, sys
readsize = 1024

def join(fromdir, tofile):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        try:
            fileobj = open(filepath, 'rb')
            while True:
                filebytes = fileobj.read(readsize)
                if not filebytes: break
                output.write(filebytes)
            fileobj.close()
        except IsADirectoryError:
            pass
    output.close()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.arg[1] == '-help':
        print('Use: join.py [from-dir-name to-file-name]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files? ')
            tofile = input('Name of files to be recreated? ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        print('Joining', absfrom, 'to make', absto)
        
        try:
            join(fromdir, tofile)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Join complete: see', absto)
        if interactive: input('Press Enter key')    # pause if clicked