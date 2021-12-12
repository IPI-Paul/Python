#!/usr/bin/env python3

# Example 5-10
# Adds a with statement around a nested block of code. The context manager 
# acquires the lock on with statement entry and releases it on statement exit 
# regardless of exception outcomes. The net effect is to save one line of code, 
# but also guarantee lock release when exceptions are possible
# Author: Mark Lutz
# Last modified: 

"""
passed in mutex object shared by all threads instead of globals; use with context
manager statement for auto acquire/release; sleep calls added to avoid busy loops
and simulate real work
"""

import _thread as thread, time
stdoutmutex = thread.allocate_lock()
numthreads = 5 
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myId, count, mutex):                    # shared object passsed in
    for i in range(count):
        time.sleep(1 /(myId + 1))                   # diff fractions of second
        with mutex:
            print('[%s] => %s' % (myId, i))
    exitmutexes[myId].acquire()                     # global: signal main thread

for i in range(numthreads):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes) : time.sleep(0.25)
print('Main thread exiting.')