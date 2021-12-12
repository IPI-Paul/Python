#!/usr/bin/env python3

# Example 12-5
# Installs a Python-coded signal handler function to respond to whatever signal 
# number you type on the command line
# Author: Mark Lutz
# Last modified: 

"""
Demo Python's signal module; pass signal number as a command-line arg, and use a
"kill -N pid" shell command to send this process a signal; on my Linux machine,
SIGUSR1=10, SIGUSR2=12, SIGCHLD=17, and SIGCHLD handler stays in effect even if 
not restored: all other handlers are restored by Python after caught, but SIGCHLD
behaviour is left to the platform's implementation; signal works on Windows too,
but defines only a few signal types; signals are not very portable in general;
"""

import sys, signal, time

def now():
    return time.asctime()

def onSignal(signum, stackframe):               # Python signal handler
    print('Got signal', signum, 'at', now())    # most handlers stay in effect
    if signum == signal.SIGCHLD:                # but sigchld handler is not
        print('sigchld caught')
        # signal.sinal(signal.SIGCHLD, onSignal) 

signum = int(sys.argv[1])
signal.signal(signum, onSignal)                 # install signal handler
while True: signal.pause()                      # sleep waiting for signals