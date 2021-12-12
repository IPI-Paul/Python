#!/usr/bin/env python3

# Example 8-35
# Uses multiprocessing module to run the GUIs as independent processes. It 
# produces the exact same windows as the previous example, except that the label 
# in the main window is different
# Author: Mark Lutz
# Last modified: 

"""
4 demo classes run as independent program processes: multiprocessing;
multiprocessing allows us to launch named functions with arguments, but not 
lambdas, because they are not pickleable on Windows; multiprocessing also has its
own IPC tools like pipes for communication
"""

from tkinter import *
from multiprocessing import Process
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def runDemo(modname):                                   # run in a new process
    module = __import__(modname)                        # build gui from scratch
    module.Demo().mainloop()

if __name__ == '__main__':
    for modname in demoModules:                         # in __main__ only!
        Process(target=runDemo, args=(modname,)).start()
    
    
    root = Tk()                                         # parent process GUI
    root.title('Processes')
    Label(root, text='Multiple program demo: multiprocessing', bg='white').pack()
    root.mainloop()