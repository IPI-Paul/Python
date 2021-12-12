#!/usr/bin/env python3

# Example 10-29
# Spawns a thread that reads the socket or pipe and places the data on a queue
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-12-19

"""
read command pipe in a thread and place output on a queue checked in timer loop;
allows script to display program's output without being blocked between its 
outputs; spawned programs need not connect or flush, but this approaches 
complexity of sockets
"""

import _thread as thread, queue, os
from tkinter import Tk, Button
from guiStreams import GuiOutput
stdoutQueue = queue.Queue()                     # infinite size

def producer(input):
    while True:
        line = input.readline()                 # OK to block: child thread
        stdoutQueue.put(line)                   # empty at end-of-file
        if not line: break

def consumer(output, root, term='<end>'):
    try:
        line = stdoutQueue.get(block=False)     # main thread: check queue
    except queue.Empty:                         # 4 times/sec, OK if empty
        pass
    else:
        if not line:                            # stop loop at end-of-file
            output.write(term)                  # else display nect line
            return
        output.write(line)
    root.after(250, lambda: consumer(output, root, term))

def redirectedGuiShellCmd(command, root):
    input = os.popen(command, 'r')              # start non-GUI program
    output = GuiOutput(root)
    thread.start_new_thread(producer, (input,)) # start reader thread
    consumer(output, root)

def launch():
    redirectedGuiShellCmd('python -u pipe-nongui.py', Tk())

if __name__ == '__main__':
    win = Tk()
    Button(win, text='Go!', command=launch).pack()
    win.mainloop()