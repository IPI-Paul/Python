#!/usr/bin/env python3

# Example 6-3
# Adss the ability to search every directory on the module import search path 
# that includes every iomportable Python-coded module on computer, located both 
# on the the path directly and nested in package directory trees
# Author: Mark Lutz
# Last modified: 

"""
Find the largest Python source file on the module import search path. Skip 
already-visited directories, normalise path and case so they will match properly,
and include line sounts in pprinted result. It's not enough to use 
os.environ['PYTHONPATH']: this is a subset of sys.path.
"""

import sys, os, pprint
trace = 0 # 1=dirs, 2=+files

visited = {}
allsizes = []
for srcdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        if trace > 0: print(thisDir)
        thisDir = os.path.normpath(thisDir)
        fixcase = os.path.normcase(thisDir)
        if fixcase in visited:
            continue
        else:
            visited[fixcase] = True
        for filename in filesHere:
            if filename.endswith('.py'):
                if trace > 1: print('...', filename)
                pypath = os.path.join(thisDir, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except os.error:
                    print('skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsizes.append((pysize, pylines, pypath))

print('By size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

print('By lines..')
allsizes.sort(key=lambda x : x[1])
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])