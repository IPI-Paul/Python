#!/usr/bin/env python3

# Example 5-17
# Forks child processes and prints child process exit statuses returned by 
# os.wait calls in the parent until a 'q' is typed at the console
# Author: Mark Lutz
# Last modified: 

"""
fork child processes to watch exit status with os.wait; fork works on Unix and 
Cygwin but not standard Windows Python 3.1; note: spawned threads share globals,
but each forked process has its own copy of them (forks share file descriptors)
--exitstat is always the same here but will vary if for threads;
"""

import os
existat = 0

def child():                            # could os.exit a script here
    global existat                      # change this priocess's global
    existat += 1                        # exit status to parent's wait
    print('Hello from child', os.getpid(), existat)
    os._exit(existat)
    print('Never reached')

def parent():
    while True:
        newpid = os.fork()              # start a new copy of process
        if newpid == 0:                 # if in copy, run child logic
            child()                     # loop until 'q' console input
        else:
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q': break

if __name__ == '__main__': parent()