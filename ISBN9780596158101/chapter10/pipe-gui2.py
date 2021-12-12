#!/usr/bin/env python3

# Example 10-28
# Creates an enclosing GUI and kicks off an event loop manually by the time the 
# shell command is spawned
# Author: Mark Lutz
# Last modified: 

# GUI reader side: like pipes-gui1, but make root window and mainloop explicit

from tkinter import *
from guiStreams import redirectedGuiShellCmd

def launch():
    redirectedGuiShellCmd('python -u pipe-nongui.py')

window = Tk()
Button(window, text='Go!', command=launch).pack()
window.mainloop()
       

