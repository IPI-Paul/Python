#!/usr/bin/env python3

# Example 5-32
# Spawns three producer threads to post to a shared queue and repeatedly polls 
# for results to appear
# Author: Mark Lutz
# Last modified: 

"""
Process class can also be subclassed just like threading.Thread; Queue works 
like queue.Queue but for cross-process, not cross-thread
"""

import os, time, queue
# process-safe shared queue. queue is a pipe + locks/semas
from multiprocessing import Process, Queue       

class Counter(Process):
    label = ' @'
    def __init__(self, start, queue):       # retain state for use in run
        self.state = start
        self.post = queue
        Process.__init__(self)
    
    def run(self):                          # run in new process on start()
        for i in range(3):
            time.sleep(1)
            self.state += 1
            print(self.label, self.pid, self.state) # self.pid is this child's pid
            self.post.put([self.pid, self.state]) # stdout file is shared by all
        print(self.label, self.pid, '-')

if __name__ == '__main__':
    print('start', os.getpid())
    expected = 9
    
    post = Queue()
    p = Counter(0, post)                # start 3 processes sharing queue
    q = Counter(100, post)              # children are producers
    r = Counter(1000, post)
    p.start(); q.start(); r.start()
    
    while expected:                     # parent consumes data on queue
        # this is essentially like a GUI, though GUIIs often use threads
        time.sleep(0.5)             
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data...')
        else:
            print('posted:', data)
            expected -= 1
    
    p.join(); q.join(); r.join()                # must get before join putter
    print('finish', os.getpid(), r.exitcode)    # exitcode is child exit status