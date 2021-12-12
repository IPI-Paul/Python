#!/usr/bin/env python3

# Example 3-3
# Demonstrates how key assignments to os.environ call os.putenv (a function that
# changes the shell variable outside the boundaries of the Python interpreter)
# Author: Mark Lutz
# Last modified: 

import os
print('setenv...', end=' ')
print(os.environ['USERNAME'])               # show current shell variable value

os.environ['USERNAME'] = 'Brian'            # returns os.putenv behind the scenes
os.system('python echoenv.py')

os.environ['USERNAME'] = 'Arthur'           # changes passed to spawned programs
os.system('python echoenv.py')           # and linked-in C library modules

os.environ['USERNAME'] = input('?')
print(os.popen('python echoenv.py').read())