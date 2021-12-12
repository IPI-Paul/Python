#!/usr/bin/env python3

# Example 20-32
# Defines two callback handler functions and imports the C extension module to 
# register handlers and trigger events
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
in Python, register for and handle event callbacks from the C language; compile 
and link the C code, and launch this with 'python register.py'
################################################################################
"""

###################################
# C calls these Python functions;
# handle an event, return a result
###################################

def callback1(label, count):
    return 'callback1 => %s number %i' % (label, count)

def callback2(label, count):
    return 'callback2 => ' + label * count

#######################################
# python calls ta C extension module
# to register handlers, trigger events
#######################################

import sys
sys.path.append('../sourceFiles/libraries')
import ch20_cregister as cregister

print('\nTest1: ')
cregister.setHandler(callback1)     # register callback function
for i in range(3):
    cregister.triggerEvent()        # simulate events caught by C layer

print('\nTest2: ')
cregister.setHandler(callback2)
for i in range(3):
    cregister.triggerEvent()        # routes these events to callback2