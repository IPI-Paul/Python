#!/usr/bin/env python3

# Example 10-13
# Shows one way to wrap the packing operation dialog of the shell GUI section's 
# Example 10-10 to force its printed output to appear in a popup window when 
# generated, instead of in the console
# Author: Mark Lutz
# Last modified: 

# wrap command-line script in GUIO redirection tool to pop up its output

from tkinter import *
from packdlg import runPackDialog
from guiStreams import redirectedGuiFunc

def runPackDialog_Wrapped():                    # callback to run in mytools.py
    redirectedGuiFunc(runPackDialog)            # wrap entire callback handler

if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)
    root.mainloop()