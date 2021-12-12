#!/usr/bin/env python3

# Example 5-4
# Demonstrates how a string of arguments passed of arguments passed to os.execlp 
# by a fork-exec script can start another Python program file
# Author: Mark Lutz
# Last modified: 

import os, sys
print('Hello from child', os.getpid(), sys.argv[1])