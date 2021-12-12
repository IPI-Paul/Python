#!/usr/bin/env python3

# Example 5-18
# Each thread changes the single shared global variable, existat
# Author: Mark Lutz
# Last modified: 

"""
spawn threads to watch shared global memory change; threads normally exit when 
the function the run returns, but _thread.exit() can be called to exit calling 
thread; _thread.exit is the same as sys.exit and raising SystemExit; threads 
communicate with possibly locked global vars; caveat: may need to make print/
input calls atomic on some platforms--shared stdout;
"""

import _thread as thread
exitstat = 0

def child():
    global exitstat                         # process global names
    exitstat += 1                           # shared by all threads
    threadid = thread.get_ident()
    print('Hello from child', threadid, exitstat)
    thread.exit()
    print('Never reached')

def parent():
    while True:
        thread.start_new_thread(child, ())
        if input() == 'q': break

if __name__ == '__main__': parent()