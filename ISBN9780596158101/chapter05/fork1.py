#!/usr/bin/env python3

# Example 5-1
# Forks new child processes until you type the letter q at the console
# Author: Mark Lutz
# Last modified: 

'forks child processes until you type "q"'

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0)     # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()