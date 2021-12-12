#!/usr/bin/env python3

# Example 2-1
# Provides a file read paging function
# Author: Mark Lutz
# Last modified: 

"""
split and interactively page a string or file of text
"""

def more(text, numlines=15):
    lines = text.splitlines()               # like split('\n') but no '' at end
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys                              # when run, not imported
    # page contents of file on cmdline
    more(open(sys.argv[1]).read(), int(sys.argv[2]))