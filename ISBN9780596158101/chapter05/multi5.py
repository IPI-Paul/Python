#!/usr/bin/env python3

# Example 5-33
# Illustrates that the program doesn't require any resources passed in by the 
# Process API, but offers a portable equivalent to the fork/exec combination on 
# Unix. Makes use of traditional IPC tools, like sockets and fifos
# Author: Mark Lutz
# Last modified: 

'Use multiprocessing to start independent programs, os.fork or not'

import os
from multiprocessing import Process

def runprogram(arg):
    if not ('__import__' in str(arg) and 'system' in str(arg)):
        os.execlp('python', 'python', 'child.py', str(arg))

if __name__ == '__main__':
    for i in range(5):
        Process(target=runprogram, args=(i,)).start()
    print('parent exit')