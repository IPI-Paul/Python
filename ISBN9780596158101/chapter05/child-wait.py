#!/usr/bin/env python3

# Example
# Further demonstrates how a string of arguments passed of arguments passed to 
# os.execlp by a fork-exec script can start another Python program file
# Author: Mark Lutz
# Last modified: 

import os, sys
print('Hello from child', os.getpid(), sys.argv[1])
input('Press <Enter>')              # don't flash on Windows