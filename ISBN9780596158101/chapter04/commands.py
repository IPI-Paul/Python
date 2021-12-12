#!/usr/bin/env python3

# Example 4-2
# Is a client script that does simple line translations
# Author: Mark Lutz
# Last modified: 

from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass

def processLine(line):                          # define a function
    if line[0] == '*':                          # applied to each line
        print('Ms.', line[1:-1])
    elif line[0] == '+':
        print('Mr.', line[1:-1])                # strip first and last char: \n
    else:
        raise UnknownCommand(line)              # raise an exception

filename = '../sourceFiles/text/ch03-data.txt'
if len(argv) == 2: filename = argv[1]           # allow filename cmd arg
scanner(filename, processLine)                  # start the scanner