#!/usr/bin/env python3

# Example 8-33
# Attaches instances of all four demo bar objects to their own independent 
# Toplevel windows, instead of the same container
# Author: Mark Lutz
# Last modified: 

"""
4 demo classes in independent top-level windows;
not processes: when one is quit all others go away, because all windows run in 
the same process here; make Tk() first here, else we get blant defualt window
"""

from tkinter import *
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)                # import by name string
        window = Toplevel()                         # make a new window
        demo = module.Demo(window)                  # parent is new window
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects

def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()

root = Tk()                                         # make explicit root first
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel Window Demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()