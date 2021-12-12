#!/usr/bin/env python3

# Example 8-14
# Is a pop-up window as a Toplevel with attached widgets, a callback handler to 
# fetch user inputs and to destroy the window but unlike Example 8-13 is nonmodal
# Author: Mark Lutz
# Last modified: 

from tkinter import *

def dialog():
    win = Toplevel()                                    # make a new window
    Label(win, text='Hard drive reformatted!').pack()   # add a few widgets
    Button(win, text='OK', command=win.quit).pack()     # set quit callback
    win.protocol('WM_DELETE_WINDOW', win.quit)          # quit on wm close
    
    win.focus_set()         # take over input focus,
    win.grab_set()          # disable other windows while I'm open,
    win.mainloop()          # and start a nested event loop to wait
    win.destroy()
    print('dialog exit')

root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()