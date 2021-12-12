#!/usr/bin/env python3

# Example 5-12
# Shows that even simple global variables can require coordination if concurrent 
# updates are possible
# Author: Mark Lutz
# Last modified: 

'prints different results on different runs on Windows 7'

import threading, time

count = 0

def adder():
    global count
    count = count + 1           # update shared name in global scope
    time.sleep(0.5)             # threads share object memory and global names
    count = count + 1

threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)

for thread in threads: thread.join()
print(count)