#!/usr/bin/env python3

# Example 6-15
# Falls back on spawning shell find commands if you have them
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-08

"""
find and delete all '*.pyc' bytecode files at and below the directory named on 
the command-line; assumes a nonportable Unix-like find command
"""

import os, sys

cygwinPath = 'c:\cygwin' if os.path.exists('c:\\cygwin') else 'c:\\cygwin64'

def ml():
    rundir = sys.argv[1]
    if sys.platform[:3] == 'win':
        findcmd = r'%s\bin\find "%s" -name "*.pyc" -print' % (cygwinPath, rundir)
    else:
        findcmd = 'find "%s" -name "*.pyc" -print' % rundir
    print(findcmd)

    count = 0
    for fileline in os.popen(findcmd):              # for all result lines
        count += 1                                  # have \n at the end
        print(fileline, end='')
        os.remove(fileline.rstrip())
    
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
    rundir = args[0]
    warning = 'Using the * only wildcard will delete all files in the' \
        ' specified directory and its subdirectories.\nDo you want to continue (Y/N): '
    if args[1] in ('*', '*.*'):
        if not input(warning).upper() == 'Y':
            exit(0)
    
    if sys.platform[:3] == 'win':
        if input('Do you have Cygwin installed? ').upper() == 'Y':
            findcmd = r'%s\bin\find "%s" -name "%s" -print' % (cygwinPath, 
                                                               rundir, args[1])
        else:
            findcmd = r'dir "%s\%s" /b /s' % (rundir, args[1])
    else:
        findcmd = 'find "%s" -name "%s" -print' % (rundir, args[1])
    print(findcmd)
    
    count = 0
    for fileline in os.popen(findcmd):              # for all result lines
        if not os.path.isdir(fileline.rstrip()): 
            count += 1                                  # have \n at the end
            print(fileline, end='')
            os.remove(fileline.rstrip())
        else:
            print('%s is a directory!' % fileline.rstrip())
    
    print('Removed %d %s files' % (count, args[1]))

if len(sys.argv) > 2:
    ipi()
elif len(sys.argv) > 1:
    ml()
else:
    print("""
Mark Lutz Usage: cleanpyc-find-shell.py path
IPI Paul Usage : cleanpyc-find-shell.py path pattern[*.pyc; *.*; */'*'; a*.*]
    """)