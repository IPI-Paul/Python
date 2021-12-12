#!/usr/bin/env python3

# Example 4-3
# Shows two approaches to changing a file while scanning: one uses explicit 
# files, and the other uses the standard input/output streamsto allow for 
# redirection on the command line
# Author: Mark Lutz
# Last modified: 

import sys

def filter_files(name, function):               # filter file through function
    input = open(name, 'r')                     # create file objects
    output = open(name + '.out', 'w')           # explicit output file too
    for line in input:
        output.write(function(line))            # write the modified line
    input.close()
    output.close()

def filter_stream(function):                    # no explicit files
    while True:                                 # use standard streams
        line = sys.stdin.readline()             # or: input()
        if not line: break
        print(function(line), end='')           # or: sys.stdout.write()

if __name__ == '__main__':
    filter_stream(lambda line: line)            # copy stdin to stdout if run