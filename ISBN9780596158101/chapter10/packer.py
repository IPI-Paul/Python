#!/usr/bin/env python3

# Example 10-7
# Concatenates the contents of multiple text files into a single file, with 
# predefined separator lines between them
# Author: Mark Lutz
# Last modified: 

# pack text file into a single file with separator line (simple archive)

import sys, glob
marker = ':' * 20 + 'textpak=>'                 # hopefully unique separator

def pack(ofile, ifiles):
    output = open(ofile, 'w')
    for name in ifiles:
        print('packing:', name)
        input = open(name, 'r').read()          # open the next input file
        if input[-1] != '\n': input += '\n'     # make sure it has endline
        output.write(marker + name + '\n')      # write a separator line
        output.write(input)                     # and write the file's contents

if __name__ == '__main__':
    ifiles = []
    for patt in sys.argv[2:]:
        ifiles += glob.glob(patt)               # not globbed auto on windows
    pack(sys.argv[1], ifiles)                   # pack files listed on cmdline