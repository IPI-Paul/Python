#!/usr/bin/env python3

# Example 8-19
# Uses the prior example's makeform and fetch functions to generate a form and 
# prints its contents, much as before. Here, though, the input fields are attached 
# to a new Toplevel pop-up window created on demand, and an OK button is added 
# to the new window to trigger a window destroy event that erases the pop up
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-18

# make from dialog modal; must fetch before destroy with entries

from tkinter import *
from entry2 import makeform, fetch, fields

def show(entries, popup):
    applyArgs(entries, sys._getframe().f_code.co_name)
    fetch(entries)                  # must fetch before window destroyed!
    popup.destroy()                 # fails with msgs if stmt order is reversed

def ask():
    global args
    popup = Toplevel()              # show form in modal dialog window
    ents = makeform(popup, fields)
    applyArgs(ents, '')
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()             # wait for destroy

def applyArgs(entries, func):
    global args
    if func == 'show':
        for i in range(len(fields)):
            args[fields[i]] = entries[i].get()
    elif len(args) > 0:
        for i in range(len(fields)):
            entries[i].insert(0, args[fields[i]])
        
root = Tk()
args = {}
Button(root, text='Dialog', command=ask).pack()
root.mainloop()