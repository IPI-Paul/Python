#!/usr/bin/env python3

# Example 5-3
# Forks new processes until we type q again, but child processes run a brand-new
# program instead of calling a function in the same file
# Author: Mark Lutz
# Last modified: 

'starts programs until you type "q"'

import os

parm = 0
while True:
    parm +=1
    pid = os.fork()
    if pid == 0:                                            # copy process
        if not ('__import__' in str(parm) and 'system' in str(parm)):
            os.execlp('python', 'python', 'child.py', str(parm))# overlay program
        assert False, 'error starting program'              # shouldn't return
    else:
        print('Child is', pid)
        if input() == 'q': break