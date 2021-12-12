#!/usr/bin/env python3

# Example 10-18
# Is the GUI equivalent of the queue-based threaded program in Exampke 5-14
# Author: Mark Lutz
# Last modified: 

# GUI that displays data produced and queued by worker threads

import _thread, queue, time
dataQueue = queue.Queue()                   # infinite size

def producer(id):
    for i in range(5):
        time.sleep(0.1)
        print('put')
        dataQueue.put('[produce id=%d, count=%d]' % (id, i))

def consumer(root):
    try:
        print('get')
        data = dataQueue.get(block=False)
    except queue.Empty:
        pass
    else:
        root.insert('end', 'consumer got => %s\n' % str(data))
        root.see('end')
    root.after(250, lambda:consumer(root))                  # 4 times per sec

def makethreads():
    for i in range(4):
        _thread.start_new_thread(producer, (i,))

if __name__ == '__main__':
    # main GUI thread: spawn batch of worker threads on each mouse click
    from tkinter.scrolledtext import ScrolledText
    root = ScrolledText()
    root.pack()
    root.bind('<Button-1>', lambda event: makethreads())
    consumer(root)                      # start queue check loop in main thread
    root.mainloop()                     # pop-up window, enter tk event loop