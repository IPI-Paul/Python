#!/usr/bin/env python3

# Example 12-12
# Illustrates how some of these complexities apply to redirected standard streams,
# by attempting to connect them to both text and binary mode files poduced by open
# and accessing them with print and input built-ins much as redirected script might
# Author: Mark Lutz
# Last modified: 

"""
test effect of connecting standard streams to text and binary mode files same 
holds true for socket.makefile: print requires text mode, but text mode precludes
unbuffered mode -- uses -u or sys.stdout.flush() calls
"""

import sys

def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = input()
    print(line)
    sys.stdin = tmp

reader(open('test-stream-modes.py'))        # works: input() returns text
reader(open('test-stream-modes.py', 'rb'))  # works: but input() returns bytes

def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp

writer(open('temp', 'w'))           # works: print() passes text str to .write()
print(open('temp').read())

try:
    writer(open('temp', 'wb'))      # FAILS on print: binary mode requires bytes
except Exception as e:
    sys.stderr.write(str(e) + '\n')
try:
    writer(open('temp', 'w', 0))    # FAILS on open: text must be unbuffered
except Exception as e:
    sys.stderr.write(str(e) + '\n')