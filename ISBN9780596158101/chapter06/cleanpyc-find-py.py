#!/usr/bin/env python3

# Example 6-16
# Does better on the portability and performance fronts and still retains code 
# simplicity, by applying the find tool written in Python in a prios session
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-08

"""
find and delte all '*.pyc' bytecode files at and below the directory named on the 
command-line; this uses a Python-coded find utility, and so is portable; run this
to delete .pyc's from an old Python release;
"""

import os, sys, find        # here, gets Tools.find

def ml():
    count = 0
    for filename in find.find('*.pyc', sys.argv[1]):
        count += 1                                  
        print(filename)
        os.remove(filename)
    
    print('Removed %d .pyc files' % count)
    
def ipi():
    args = [sys.argv[1]] if len(sys.argv) > 1 else [os.getcwd()]
    args += [sys.argv[2]] 
    if len(sys.argv) > 3: 
        args[1] = '*'
    elif not sys.platform[:3] == 'win':
        wildcard = False
        for item in sys.argv:
            if '*' in item: wildcard = True
        if wildcard == False:
            if input('Are you using the * only wildcard (Y/N)? ').upper() == 'Y':
                args[1] = '*'
    warning = 'Using the * only wildcard will delete all files in the' \
        ' specified directory and its subdirectories.\nDo you want to continue (Y/N): '
    if args[1] in ('*', '*.*'):
        if not input(warning).upper() == 'Y':
            exit(0)

    count = 0
    for filename in find.find(args[1], args[0]):
        if not os.path.isdir(filename): 
            count += 1                                  
            print(filename)
            os.remove(filename)
        else:
            print('%s is a directory!' % filename)
    
    print('Removed %d %s files' % (count, args[1]))

if len(sys.argv) > 2:
    ipi()
elif len(sys.argv) > 1:
    ml()
else:
    print("""
Mark Lutz Usage: cleanpyc-find-py.py path
IPI Paul Usage : cleanpyc-find-py.py path pattern[*.pyc; *.*; */'*'; a*.*]
    """)