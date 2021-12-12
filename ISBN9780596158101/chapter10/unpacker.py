#!/usr/bin/env python3

# Example 10-8
# Scans archives files created by the first, to unpack into individual files again
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-12-07

# unpack files created by packer.py (simple textfile archive)

import sys, os
from packer import marker                   # use common separator key
mlen = len(marker)                          # filenames after markers

def unpack(ifile, prefix='new-'):
    for line in open(ifile):                # for all input lines
        if line[:mlen] != marker:
            output.write(line)              # write real lines
        else:
            path = (line[mlen:-1].replace('\\',os.sep)).split(os.sep)
            fileName = prefix + path[-1]
            #name = prefix + line[mlen:-1]   # or make new output
            name = ''.join(x + os.sep for x in path[:-1]) + fileName
            print('creating:', name)
            output = open(name, 'w')

if __name__ == '__main__': unpack(sys.argv[1])