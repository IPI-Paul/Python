#!/usr/bin/env python3

# Example 5-5
# Spawns threads until you reply with a q at the console; it's similar in spirit
# to (and a bit simpler than) the script in Example 5-1, but it goes parallel 
# with threads instead of process forks
# Author: Mark Lutz
# Last modified: 

'spawn threads until you type "q"'

import _thread

def child(tid):
    print('Hello from thread', tid)
    
def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break

parent()