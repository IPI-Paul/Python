#!/usr/bin/env python3

# Example 5-6
# Starts 5 copies of its counter function running in parallel threads
# Author: Mark Lutz
# Last modified: 

"""
thread basics: start 5 copies of a function running in parallel; uses time.sleep 
so that the main thread doesn't die too early--this killd all other threads on 
some platforms; stdout is shared: thread outputs may be intermixed in this 
version arbitrarily
"""

import _thread as thread, time

def counter(myId, count):                           # function run in threads
    for i in range(count):
        time.sleep(1)                               # simulate real work
        print('[%s] => %s' % (myId, i))

for i in range(5):                                  # spawn 5 threads
    thread.start_new_thread(counter, (i, 5))        # each thread loops 5 times
    
time.sleep(6)
print('Main thread exiting.')                       # don't exit too early