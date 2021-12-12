#!/usr/bin/env python3

# Example 5-35
# Makes the similarity to Unix programming patters more obvious. It launches a 
# program with a fork/exec combination on Unix-like platforms (including Cygwin), 
# or an os.spawnv call on Windows
# Author: Mark Lutz
# Last modified: 

"""
start up 10 copies of child.py running in parallel; use spawnv to launch a 
program on Windows (like fork+exec); P_OVERLAY replaces, P_DETACH makes child 
stdout go nowhere; or use portable subprocess or multiprocessing options today!
"""

import os, sys

for i in range(10):
    if sys.platform[:3] == 'win':
        pypath = sys.executable
        os.spawnv(os.P_NOWAIT, pypath, ('python', 'child.py', str(i)))
    else:
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned' % pid)
        else:
            if not ('__import__' in str(i) and 'system' in str(i)):
                os.execlp('python', 'python', 'child.py', str(i))
print('Main process exiting.')