#!/usr/bin/env python3

# Example 5-28
# Sets an alarm and installs a SIGALRM handler
# Author: Mark Lutz
# Last modified: 

"""
set and catch alarm timeout signals in Python; time.sleep doesn't play well with 
alarm (or signal in general on some Linux PCs), so we call signal.pause here to 
do nothing until a signal is received
"""

import sys, signal, time
def now(): return  time.asctime()

def onSignal(signum, astackframe):              # python signal handler
    print('Got alarm', signum, 'at', now())     # most handlers stay in effect

while True:
    print('Setting at', now())
    signal.signal(signal.SIGALRM, onSignal)     # install signal handler
    signal.alarm(5)                             # do signal in 5 seconds
    signal.pause()                              # wait for signals