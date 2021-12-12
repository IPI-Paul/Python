#!/usr/bin/env python3

# Example 8-4
# Demonstrates that technically you can suppress the default root creation logic 
# and make multiple root windows with the TK widget
# Author: Mark Lutz
# Last modified: 

import tkinter
from tkinter import Tk, Button

tkinter.NoDefaultRoot()

win1 = Tk()                         # two independent root windows
win2 = Tk()

Button(win1, text='Spam', command=win1.destroy).pack()
Button(win2, text='SPAM', command=win2.destroy).pack()
win1.mainloop()