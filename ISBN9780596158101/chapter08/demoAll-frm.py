#!/usr/bin/env python3

# Example 8-32
# Illustrates hierarchical GUI composition on a grander scale than previous 
# examples. Arranges to show all four of the dialog launcher bar scripts of this
# chapter in a single container
# Author: Mark Lutz
# Last modified: 

"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this window too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""

from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)                   # import by name string
        part = module.Demo(root)                    # attach an instance
        part.config(bd=2, relief=GROOVE)            # or pass configs to Demo()
        part.pack(side=LEFT, expand=YES, fill=BOTH) # grow, stretch with window
        parts.append(part)                          # change list in-place
    
def dumpState():
    for part in parts:                              # run demo report is any
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')

root = Tk()                                         # make explicit root first
root.title('Frames')
Label(root, text='Multiple Frame Demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()